from streamlit_option_menu import option_menu
import streamlit as st 
from plyer import notification

class Principal:
    def __init__(self,*args):
        self.seleçao=args
        self.texto=""
        self.email=args
        self.telefone=args
        self.Comprovante=args
        self.comprovante=args
        self.option_menu=args
        self._component_func=args
        with st.sidebar:
            seleçao = st.selectbox("Advogacia Online",["INÍCIO","QUEM SOMOS","DÚVIDAS JURÍDICAS","CONSULTAS JURÍDICAS","ÁREA VIP","CÁMERA","ARTIGOS","MENSAGENS"])
                
        #################################### CONFIGURAÇOES DOS COMPONENTES #########################################


        ################## QUEM SOMOS #####################################################################   
        if seleçao == "QUEM SOMOS":
            st.subheader("Quem Somos")
            st.write("""Aplicativo júridico criado com o ituito de propagar, o conhecimento, 
                    bem como, proporcionar todo o suporte júridico necessário ao cidadao.\n
                    Atendimento ao cliente como se estivesse dentro de um escritório de advogacia.\n
                    Os profissionais sao habilitados perante a OAM""")
        ################ MENU DUVIDAS #####################################################################

        if seleçao =="DÚVIDAS JURÍDICAS":
            
            st.subheader("DÚVIDAS JURÍDICAS")
            st.markdown('---')
            st.write("""Sao questionamentos simples, rápido, que nao denotam a análise de documentos.Para esclarecer uma dúvida""")
            st.markdown('---')
            
        ###############  EXPANDER #########################################################################
            with st.expander("Siga os passos abaixo:"): 
                st.write("""
                    1. Efectue o pagamento no valor de: 0,00 Mts\n
                    2. Salve o comprovativo do pagamento.\n
                    3. Preencha os campos abaixo com sua duvida e envie o comprovativo.\n
                    Sua dúvida sera esclarecida em até 24 horas úteis,
                    após a confirmaçao o pagamento. 
                        """)
                
        ########### FORMULÁRIO ###########################################################################

            st.subheader("FORMULÁRIO")
            with st.form(key="col1",clear_on_submit=True):
            
                col1, col2 = st.columns([2,3])
                with col1:
                    st.write("Preencha após o pagamento acima")
                    nome=st.text_input("Nome*")
                    self.email=st.text_input("E-mail*")
                    self.telefone=st.text_input("Telefone*")
                    botao = st.form_submit_button("Enviar")
                    if botao == True:
                        notification.notify(title="Alerta",message="Voce tem uma nova mensagem de\n"+ nome ,timeout=1,app_name="Code-Mind",app_icon="cod.ico",ticker="CODE-MIND")
                
        # CAIXA DE TEXTO ###############################
                
                with col2:
                    self.texto=st.text_area("Qual é a sua dúvida*")
                    self.Comprovante = st.file_uploader("Anexar comprovante*")
            st.markdown('---')
            
        ############ MENU CONSULTAS #########################################################################
        if seleçao=="CONSULTAS JURÍDICAS":
        
            st.subheader("Consulta Jurídica")
            st.text("""Envolve análise de documentos e consiste em interpretaçao e aplicaçao da legislaçao jurídica,\n em questoes de razoável complexibilidade.\nPara solicitar uma consulta jurídica. 
                """)
            st.markdown('---')
            
        ###############  EXPANDER ###########################################################################
            with st.expander("Siga os passos abaixo:"): 
                st.write("""
                    1. Efectue o pagamento no valor de: 0,00 Mts\n
                    2. Salve o comprovativo do pagamento.\n
                    3. Preencha os campos abaixo com suas duvidas e envie o comprovativo.\n
                    Sua dúvida sera esclarecida em até 3 dias úteis,
                    após o pagamento e recepçao do documento
                        """)
        
        ########### FORMULÁRIO ##############################################################################

            st.write(":orange[Pagar com:]")
            
            st.subheader("FORMULÁRIO")
            with st.form(key="form",clear_on_submit=True):
            
                col1, col2 = st.columns([2,3])
                with col1:
                    st.write("Preencha após o pagamento acima")
                    nome=st.text_input("Nome*")
                    self.email=st.text_input("E-mail*")
                    self.telefone=st.text_input("Telefone*")
                    botao = st.form_submit_button("Enviar")
                    if botao == True:
                        notification.notify(title="Alerta",message="Voce tem uma nova mensagem de\n"+ nome ,timeout=1,app_name="Code-Mind",app_icon="cod.ico",ticker="CODE-MIND",toast=True)
                        
########################### TEXT AREA ##########################################################################
                with col2:
                    self.texto=st.text_area("Qual é a sua dúvida*",value=self.texto)
                    #st.write("Comprovante*")
                    self.comprovante = st.file_uploader("Anexar comprovante*")
                
        if seleçao =="ÁREA VIP":
            st.header(":orange[Clientes com contratos]")
        ########### COLUNAS DE ARTIGO ##############################################################################
        if seleçao =="ARTIGOS":
            st.subheader("Artigos")
            col1, col2, col3, col4, col5 =st.columns(5)
            with col1:
                with st.expander("Casamento e uniao estável-quais os efeitos?"):
                    st.write("")
            with col2:
                with st.expander("Casamento e uniao estável-como se extingue?"):
                    st.write("")
            with col3:
                with st.expander("Entenda o que é casamento e uniao estável"):
                    st.write("")
            with col4:
                with st.expander("Conheça os efeitos do assédio moral"):
                    st.write("")
            with col5:
                with st.expander("Ássedio moral, voce sabe o que significa?"):
                    st.write("")
        if seleçao =='CÁMERA':
            foto = st.camera_input("Tirar Foto")
            cl1, cl2 =st.columns(2)
            with st.expander("Ver Imagem"):
                with cl1:
                    if foto:
                        st.image(foto)
                        st.write("Ver as imagens")
                
                    
        if seleçao=="MENSAGENS":
            st.header(":orange[As mensagens dos clientes serao mostradas aqui]")
            st.text_area("Mensagens", value=self.texto)

        if seleçao=="INÍCIO":
            st.title(":orange[TELA INICIAL]")

        hide="""
        <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden}
            footer {visibility: hidden;}
        </style>    
        """
        st.markdown(hide,unsafe_allow_html=True)
Principal()
