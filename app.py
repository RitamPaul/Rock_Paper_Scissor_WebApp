import streamlit as st
import random
import datetime

fullform = {1:'rock', 2:'paper', 3:'scissor'}
defeat = {'rock':'scissor', 'paper':'rock', 'scissor':'paper'}
symbol = {'rock':'🪨', 'paper':'📰', 'scissor':'✂️'}

# initialising cache data
for attrib in ['humanwin','cscore','hscore','ind']:         # integer variables
    if attrib not in st.session_state:
        st.session_state[attrib] = 0
if 'humanchoice' not in st.session_state:                   # string variables
    st.session_state['humanchoice'] = None
if 'history' not in st.session_state:                       # list variables
    st.session_state['history'] = list(dict())


ind = st.session_state['ind']
humanchoice = st.session_state['humanchoice']


# win / loss message + displating score
scoremesg = f'Your score - {st.session_state['hscore']} | Computer score - {st.session_state['cscore']}'
if (humanchoice!=None) and (humanchoice!='EXIT'):
    if (st.session_state['humanwin'] == 1):
        st.success(f'**Congratulations, you\'ve won last battle --> {scoremesg}**', icon='🏆')
    elif (st.session_state['humanwin'] == 0):
        st.warning(f'**Last battle is a DRAW --> {scoremesg}**', icon='🌓')
    elif (st.session_state['humanwin'] == -1):
        st.error(f'**Oops! Computer has won last battle --> {scoremesg}**', icon='😟')


if humanchoice=='EXIT':
    st.success('Thanks for visiting. Come again', icon='🌸')
else:
    writingspace = st.container(height=450, border=True)
    with writingspace:
        # welcome message
        with st.chat_message(name='🤖'):
            st.write('**Welcome here, Lets start the game**')
        
        if humanchoice != None:
            # displaying previous all history
            for mesg in st.session_state['history']:
                with st.chat_message(name = f'{mesg['icon']}'):
                    st.write(f'{mesg['text']}')

col1, col2 = st.columns([0.6,0.4], gap='small', vertical_alignment='center')

with col1:
    st.subheader(
        '**Enter your choice 👉🏻**' if (humanchoice!='EXIT') else '**Reload to continue 😃**'
    )

with col2:
    # user input
    if st.selectbox(
        label='',
        key=f'choice-{ind}',
        options=['rock','paper','scissor','EXIT'],
        index=None,
        placeholder='choose from here' if (humanchoice!='EXIT') else ('reload required'),
        label_visibility='collapsed',
        disabled=humanchoice=='EXIT'
    ):
        humanchoice = st.session_state[f'choice-{ind}']
        del st.session_state[f'choice-{ind}']
        
        st.session_state['humanchoice'] = humanchoice
        st.session_state['ind'] = not st.session_state['ind']
        
        if (humanchoice != 'EXIT'):
            # saving human choice in cache
            curtime = datetime.datetime.now().strftime('%H:%M:%S')            
            mesg = {'icon':'🤠', 'text':f'[{curtime}]  **You chooses - {humanchoice} {symbol[humanchoice]}**'}
            st.session_state['history'].append(mesg)

            
            
            # generating computer choice & saving in cache
            number = random.randint(1,3)
            computerchoice = fullform[number]
            curtime = datetime.datetime.now().strftime('%H:%M:%S')            
            mesg = {'icon':'🤖', 'text':f'[{curtime}]  **Computer chooses - {computerchoice} {symbol[computerchoice]}**'}
            st.session_state['history'].append(mesg)

            
            
            # judging who wins & saving in cache
            if (humanchoice != computerchoice):
                if (defeat[humanchoice] == computerchoice):
                    st.session_state['humanwin'] = 1
                    st.session_state['hscore'] += 1
                else:
                    st.session_state['humanwin'] = -1
                    st.session_state['cscore'] += 1
            else:
                st.session_state['humanwin'] = 0
        
        st.rerun()