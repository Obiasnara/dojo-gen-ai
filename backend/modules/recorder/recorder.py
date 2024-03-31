import streamlit as st
from backend.modules.recorder.utils.embed_and_save_chunks import embed_and_save_chunks
from backend.modules.recorder.utils.generate_chunks import generate_chunks
from backend.modules.recorder.utils.get_answer import get_answer

from backend.modules.recorder.utils.get_recorded_audio import get_recorded_audio
from backend.modules.recorder.utils.get_relevant_chunks import get_relevant_chunks
from backend.modules.recorder.utils.get_transcription import get_transcription


def recorder():
    """
    Render the Audio Recorder page.
    """
    st.title("Audio Recorder")
    st.write("\n\n")

    audio_data = get_recorded_audio()  # That's it! :D

    # Add some spacing and informative messages
    col_info, col_space = st.columns([0.57, 0.43])

    with col_info:
        st.write("\n" * 2)  # Add vertical spacer

    if audio_data is not None:
        # write audio data
        transcriptedData = get_transcription(audio_data)
        
        transcription_chunks = generate_chunks(transcriptedData["text"])
        embed_and_save_chunks(transcription_chunks)
        print("Texte analysé")
        question = st.text_input(label="Texte analysé, posez une question dans le champ ci dessous", placeholder="")
        context = get_relevant_chunks(question);
        print("Contexte :")
        print(context)
        if question:
            answers = []
            for t in context:
                message = f"""
                Context: {t}
                Question: {question}
                Answer:
                """
                
                response = get_answer(message)
                answers.append(response)
            print("Openai answers :")
            print(answers)
            st.write("\n\n")
            st.write("Chat bot answers: ")
            for an in answers:
                st.write(an)
                st.write("\n")