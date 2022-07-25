import spacy
nlp = spacy.load('en_core_web_sm')
from spacy import displacy
import streamlit as st
st.title('Information Extraction')
sentence = st.text_input("Enter input")

sentence_doc = nlp(sentence)

ok = st.button("Sumbit")
if ok:    
    disp = displacy.render(sentence_doc, style = 'ent', jupyter = False)
    st.markdown(disp, unsafe_allow_html=True)    
   
    

ok2 = st.button('View Dependency Graph')
if ok2:
    new_title = '<p style="font-family:sans-serif; font-size: 20px;">Dependency Graph Visualizer</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    dep_svg = displacy.render(sentence_doc, style="dep", jupyter=False)
    st.image(dep_svg, width=400, use_column_width="never")






