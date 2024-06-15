import streamlit as st

st.title('Simple Quiz Application')

if 'questions' not in st.session_state:
    st.session_state.questions = []

if 'answers' not in st.session_state:
    st.session_state.answers = []

st.header('Create a Quiz')
question = st.text_input('Question')
options = st.text_area('Options (comma-separated)').split(',')
correct_answer = st.selectbox('Correct Answer', options)

if st.button('Add Question'):
    st.session_state.questions.append({
        'question': question,
        'options': options,
        'answer': correct_answer
    })

st.write(st.session_state.questions)

st.header('Take the Quiz')
if st.session_state.questions:
    score = 0
for q in st.session_state.questions:
        st.subheader(q['question'])
        user_answer = st.radio('Options', q['options'])
        if st.button('Submit Answer'):
            st.session_state.answers.append(user_answer)
            if user_answer == q['answer']:
                score += 1
st.write(f'Your score: {score}/{len(st.session_state.questions)}')
