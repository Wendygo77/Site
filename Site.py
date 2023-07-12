import streamlit as st
from PIL import Image
import os

lore, mapa, seitas = st.tabs(["Lore", "Mapa" , 'Seitas'])

with lore:
    st.title(':blue[Asfagus-RPG]')
    st.header('Venha conhercer mais sobre o Universo de Asfagus')
    st.subheader('Lore abaixo:')
    st.title(':blue[The Rupture]')
    st.markdown('Em eras ancestrais, muito antes da magia ser criada e descoberta, três entidades de pura energia arcana unificaram-se em um único ser.') 
                
    st.markdown('Milênios após a unificação o ser ancestral que originou-se da unificação estava completamente perdido, entrando em conflito com a realidade e caindo cada vez mais em um vazio existencial. Smalph, assim chamado, teve por fim um surto.Cada entidade era capaz de pensar por conta própria, mesmo dividindo um único corpo.')
    st.markdown('Após um desentendimento entre Corvus e Saiph, os seres ancestrais travaram uma guerra entre seus pesadelos e sonhos, e quem ganhasse teria total controle sobre o corpo principal. Com séculos de uma batalha incansável, eles entraram em um estado de colapso.') 
    st.markdown('Uma das três entidades, com medo do que poderia acontecer, pensou em algo para resolver de vez a guerra entre Lubus e Corvus.Saiph percebeu que era obrigado a interferir, caso contrário ele iria sucumbir junto. Para evitar isso, ele criou um prisma que sugava os poderes de Lubus e Corvus.') 
    st.markdown('Seu plano deu certo por milênios, e como grande parte do poder deles estava canalizado no prisma, Lubus e Corvus acabaram adormecendo por séculos.') 
    st.markdown('Saiph assumiu de vez a consciência e pôde vigiar o portão da floresta despreocupado.Após anos de puro tédio, ele resolveu aproveitar parte do poder que estava armazenado no prisma para dar origem a tudo que envolve magia no reino - seja criatura ou feitiço - seu poder era extraordinário. Por milênios, ele foi o grande ancião que manteve os portões que abrem caminho para o lado obscuro da floresta trancafiados.') 
    st.markdown('No início, ele controlava e manipulava cada fração de energia que era emanada pelo prisma.Após o rompimento da coalizão, Lubus e Corvus tentaram retomar a consciência. O prisma se fragmentou e Smalph se dividiu em três entidades novamente. Essas entidades deram origem às três grandes seitas que representam cada entidade antes da união.Os resquícios do prisma estão escondidos no núcleo de uma árvore que fica exatamente na divisa entre o horrendo e o agradável; seus fragmentos permanecem intocados até hoje. Os antigos dizem que a floresta é amaldiçoada e contém mistérios que ainda não foram revelados.') 
    st.markdown('Caso esses mistérios sejam desvendados, algo grandioso e com um poder inimaginável poderá surgir de Growgudor, um lugar onde nem mesmo Saiph, Lubus e Corvus podem ousar entrar.')

with mapa:
    st.title('Mapa do reino de Asfagus')
    image = Image.open(os.path.join('img','mapadeasfagus.jpg'))
    st.image(image, caption='Mapa do reino de Asfagus.')

    st.markdown('---')
with st.container():
    with seitas:
        st.title(':blue[Origem das seitas]')
        st.write('A origem das seitas é dada quando um deus antigo se dividiu em três entidades, sendo elas: Corvus, Lubus, Saiph. Depois de anos , os descendentes  dessas entidades criaram as seitas para seus seguidores.')
        image = Image.open(os.path.join('img','Saiph.jpg'))
        st.image(image, caption='O deus Saiph.')
        st.markdown('---')
        lubus, saiph, corvus = st.tabs(["Lubus", "Saiph" , 'Corvus'])
        with lubus:
            st.header(':blue[Deusa Lubus]')
            image = Image.open(os.path.join('img','DeusaLubus.jpg'))
            st.image(image, caption='Deusa Lubus.')
            st.subheader(':blue[Seita de Lubus]')
            st.markdown('A seita originou-se pela vereção que os povos do passado tinham pela deusa da inspiração Lubus,ela deu origem a  seita de Lubus que é representada por este símbolo:')
            image = Image.open(os.path.join('img','SeitasLubus.jpg'))
            st.image(image, caption='Seita de Lubus.')
            st.markdown('---')
        with saiph:
            st.header(':blue[Deus Saiph]')
            image = Image.open(os.path.join('img','DeusSaiph.jpg'))
            st.image(image, caption='Deus Saiph.')
        
            st.subheader(':blue[Seita de Saiph ]')
            st.markdown('A seita originou-se pela veneração que os povos do passado tinham pelo deus do equilíbrio Saiph, ele deu origem a seita de Saiph que é representada por este símbolo:')
            image = Image.open(os.path.join('img','SeitaSaiph.jpg'))
            st.image(image, caption='Seita de Saiph.')
            st.markdown('---')
        with corvus:
            st.header(':blue[Deus Corvus]')
            image = Image.open(os.path.join('img','DeusCorvus.jpg'))
            st.image(image, caption='Deus Corvus.')
        
            st.subheader(':blue[Seita de Corvus ]')
            st.markdown('A seita originou-se pela veneração que os povos do passado tinham pelo deus da dualidade corvus, que deu origem a seita de Corvus que é representada por este símbolo:')
            image = Image.open(os.path.join('img','SeitaCorvus.jpg'))
            st.image(image, caption='Seita de Saiph.')
            st.markdown('---')
with st.container():
    st.subheader(':red[Entre no grupo do whatsapp clicando em:] [  Quero entrar](https://chat.whatsapp.com/JxfLoBKfU7W1efSTJgG5LU)')


    st.header('Escute essa playlist animal enquanto conhece nosso RPG: ')
    st.video('https://youtu.be/j6niFit62ss')
    add_selectbox = st.sidebar.selectbox(
        "Como você gostaria de ser contactado?",
        ("Email", "Home phone", "Mobile phone")
    )