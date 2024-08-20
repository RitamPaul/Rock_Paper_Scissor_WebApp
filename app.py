import streamlit as st
import random

fullform = {1:'rock', 2:'paper', 3:'scissor'}

# initialising cache data
for attrib in ['cscore','hscore','ind']:        # integer variables
    if attrib not in st.session_state:
        st.session_state[attrib] = 0
if 'choice' not in st.session_state:            # string variables
    st.session_state['choice'] = None
if 'history' not in st.session_state:           # list variables
    st.session_state['history'] = list(dict())

ind = st.session_state['ind']
choice = st.session_state['choice']

if choice=='EXIT':
    st.warning('Thanks for visiting. Come again', icon='🌸')
else:
    writingspace = st.container(height=450, border=True)
    with writingspace:
        # welcome message
        with st.chat_message(name='🤖'):
            st.write('**Welcome here, Lets start the game**')
        
        if choice != None:
            # displaying previous all history
            for mesg in st.session_state['history']:
                with st.chat_message(name = f'{mesg['icon']}'):
                    st.write(f'**{mesg['text']}**')

            # printing score
            st.write(f'**Your score - {st.session_state['hscore']} | Computer score - {st.session_state['cscore']}**')

col1, col2 = st.columns([0.6,0.4], gap='small', vertical_alignment='center')

with col1:
    st.subheader(
        '**Enter your choice 👉🏻**' if (choice!='EXIT') else '**Reload to continue 😃**'
    )

with col2:
    # user input
    if st.selectbox(
        label='',
        key=f'humanchoice-{ind}',
        options=['rock','paper','scissor','EXIT'],
        index=None,
        placeholder='choose from here' if (choice!='EXIT') else ('reload required'),
        label_visibility='collapsed',
        disabled=choice=='EXIT'
    ):
        choice = st.session_state['choice'] = st.session_state[f'humanchoice-{ind}']
        del st.session_state[f'humanchoice-{ind}']
        st.session_state['ind'] = not st.session_state['ind']
        
        # saving human choice in cache
        mesg = {'icon':'🤠', 'text':f'You chooses - {choice}'}
        st.session_state['history'].append(mesg)

        # saving computer choice in cache
        computer = fullform[random.randint(1,3)]
        mesg = {'icon':'🤖', 'text':f'Computer chooses - {computer}'}
        st.session_state['history'].append(mesg)
        
        st.rerun()