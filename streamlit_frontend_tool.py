# We are here, adding a feature called "Tool" from langgraph




import streamlit as st
from langgraph_tool_backend import chatbot, retrieve_all_threads
from langchain_core.messages import HumanMessage, AIMessage
import uuid

# ************************************* Utility Functions ***********************************

def generate_thread_id(): 
    thread_id = uuid.uuid4() 
    return thread_id

def reset_chat(): 
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state["message_history"] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state["chat_threads"].append(thread_id)

def load_conversation(thread_id):
    return chatbot.get_state(config={"configurable": {"thread_id": thread_id}}).values["messages"]

# ************************************* Session Setup ***************************************

if "message_history" not in st.session_state:
    st.session_state['message_history'] = []

if "thread_id" not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if "chat_threads" not in st.session_state:
    st.session_state["chat_threads"] = retrieve_all_threads() # Sirf yaha par hume backend se puchhna padega ki already jitne threads exists karte hai, like ["thread-1", "thread-2"]

add_thread(st.session_state['thread_id']) 


# ************************************ Sidebar UI ****************************************

st.sidebar.title("LangGraph Chatbot")

if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("My Conversations")

for thread_id in st.session_state['chat_threads'][::-1]: # Jo conversation recent hai wah pehle dikhega.
    if st.sidebar.button(str(thread_id)): 
        st.session_state['thread_id'] = thread_id 
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage): 
                role = "user"
            else:
                role = "assistant"
            
            temp_messages.append({"role": role, "content": msg.content}) 

        st.session_state['message_history'] = temp_messages


# ************************************* Main UI *******************************************

for message in st.session_state['message_history']: 
    with st.chat_message(message["role"]): 
        st.text(message["content"])


user_input = st.chat_input("Type Here.")

if user_input:

    st.session_state['message_history'].append({"role": "user", "content": user_input})  
    with st.chat_message("user"): 
        st.text(user_input)


    CONFIG = {"configurable": {"thread_id": st.session_state['thread_id']}}

    with st.chat_message("assistant"):
        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            ):
                if isinstance(message_chunk, AIMessage):
                    # yield only assistant tokens
                    yield message_chunk.content # Is condition ka yahi matlab huwa ki, agar AIMessage hoga tabhi, stream karna. Otherwise mat karna

        ai_message = st.write_stream(ai_only_stream())

    st.session_state['message_history'].append({"role": "assistant", "content": ai_message}) 


# THREAD TRACING --> [Tracing Projects (click on the project) --> Threads on the right side of "Runs"] 
# For Every "Thread" creates a "thread" on the "Thread" option


# Here is a problem we can't see which tool is used to give answer
