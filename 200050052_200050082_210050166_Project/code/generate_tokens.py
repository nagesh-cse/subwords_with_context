import streamlit as st
import sys
import pickle
import os

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ['en', 'hi', 'mr']:
        print('ERROR : Pass language code [en or hi or mr]')
    folder = ''
    if sys.argv[1] == 'en':
        folder = './english'
    elif sys.argv[1] == 'hi':
        folder = './hindi'
    else:
        folder = './marathi'

    with open(os.path.join(folder, 'final_sg_bpe.model'), 'rb') as model_file:
        sg_bpe_model = pickle.load(model_file)
    with open(os.path.join(folder, 'final_vanilla_bpe.model'), 'rb') as model_file:
        bpe_model = pickle.load(model_file)
    
    # GUI testing
    sentence = st.text_input("Enter a sentence")
    if sentence:
        bpe_tokens_ints = bpe_model.encode(sentence, out_type=int)
        bpe_tokens = ' '.join([bpe_model.id_to_piece(x) for x in bpe_tokens_ints])

        sg_bpe_tokens_ints = sg_bpe_model.encode(sentence, out_type=int)
        sg_bpe_tokens = ' '.join([sg_bpe_model.id_to_piece(x) for x in sg_bpe_tokens_ints])

        output = ""
        output += "BPE" + "     :     " + bpe_tokens + "\n\n "
        output += "SaGe" + "     :     " + sg_bpe_tokens
        st.write("Output:\n\n " + output)
