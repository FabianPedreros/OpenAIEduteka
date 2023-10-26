import os
import openai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title='Creacion de proyectos de aprendizaje')
st.header('Crea tu proyecto de aprendizaje')
st.markdown('''Crea tus proyectos de clase ayudado por la Inteligencia Artificial. 
            Necesitarás ingresar una información base y te ayudaremos con ideas que 
            más tarde podrás refinar y modificar según tus necesidades y conocimiento.''')

st.markdown('Vamos a determinar el tema del proyecto para **Educación Superior**')

st.markdown('### Paso 1: Área académica y Asignatura.')

lst_area_academica = ['Bellas Artes', 'Ciencias Agropecuarias', 'Ciencias de la Educacion', 'Ciencias de la Salud',
                      'Ciencias Exactas y Naturales', 'Ciencias Sociales y Humanas', 'Economia, Administracion y Contaduria', 'Ingenieria' ] 

lst_asignatura = {
    'Bellas Artes' : ['Arquitectura', 'Artes audiovisuales', 'Artes escenicas', 'Artes plasticas', 'Cine y TV', 'Dibujo', 'Fotografia', 'Gastronomia', 'Musica', 'Urbanismo'], 
    'Ciencias Agropecuarias' : ['Agronomia', 'Ingenieria Agricola', 'Ingenieria Agroindustrial', 'Ingenieria Agronomica', 'Zootecnia'], 
    'Ciencias de la Educacion' : ['Educacion general', 
                                  'Licenciatura en ciencias naturales y educacion ambiental', 
                                  'Licenciatura en ciencias sociales', 
                                  'Licenciatura en educacion artistica y cultural',
                                  'Licenciatura en educacion basica primaria',
                                  'Licenciatura en educacion fisica, recreacion y deporte',
                                  'Licenciatura en matematicas'], 
    'Ciencias de la Salud' : ['Bacteriologia y laboratorio clinico', 
                              'Enfermeria', 
                              'Farmacia',
                              'Medicina',
                              'Nutricion y salud'],
    'Ciencias Exactas y Naturales' : ['Astronomia', 
                                      'Biologia', 
                                      'Ciencia de datos', 
                                      'Estadistica',
                                      'Matematicas',
                                      'Quimica'], 
    'Ciencias Sociales y Humanas' : ['Antropometria', 
                                     'Ciencia politica',
                                     'Comunicacion',
                                     'Derecho',
                                     'Periodismo'], 
    'Economia, Administracion y Contaduria' : ['Administracion', 
                                               'Economia', 
                                               'Finanzas', 
                                               'Gestion del talento humano', 
                                               'Mercadeo'], 
    'Ingenieria' : ['Diseno', 
                    'Ingenieria ambiental', 
                    'Ingenieria civil', 
                    'Ingenieria sistemas', 
                    'Ingenieria electronica', 
                    'Ingenieria industrial'] 
    }

area_academica = st.selectbox('Área académica', 
                              lst_area_academica)

if area_academica:
    opc_asignatura = lst_asignatura[area_academica]
    asignatura = st.selectbox('Asignatura',
                              opc_asignatura)
    
st.markdown('### Paso 2: Caracteristicas del proyecto.')

lst_metodo = ['Aprendizaje basado en proyectos', 'Aprendizaje basado en problemas', 'Aprendizaje basado en investigacion']

metodologia = st.selectbox('Escoja la metodologia', lst_metodo)

fases = st.text_input('Cuantas fases tiene el proyecto:')

st.markdown('### Paso 3: Cuál es el tema del Proyecto.')

tema_pincipal = st.text_area('Escribe el tema específico del proyecto:')

st.markdown('### Paso 4: Información Adicional.')

objetivo = st.text_area('Que cumpla con el siguiente objetivo de aprendizaje:')
temas = st.text_area('Que incluya los siguientes temas:')

openai.api_key = os.getenv('OPENAI_API_KEY')

if st.button('Construir proyecto de aprendizaje'):

    with st.spinner('Creando el proyecto...'):

        preprompt = f'''
        Eres un asistente universitario que ayuda a crear proyectos educativos para Educación Superior, 
        recibes indicaciones base de parte de un profesor y debes generar proyectos muy bien organizados 
        y descritos que ayudan a cumplir el tema planteado.

        Debes crear un programa educativo para el área de conocimiento de {area_academica}, específicamente para 
        estudiantes del programa de {asignatura}. 

        Debes tener en cuenta las características deseadas del programa a crear, como que la metodología de 
        enseñanza a usar es {metodologia}, por lo que debes incluir aspectos específicos de 
        la metodología seleccionada.  Este proyecto se piensa realizar en {fases} sesiones.

        El tema específico del proyecto es {tema_pincipal}, 
        este debe cumplir con el siguiente objetivo de aprendizaje {objetivo}

        Asi como incluir temas adicionales como: {temas}

        '''

        intro_prompt = '''
        Dame la introducción del proyecto planteado, ten en cuenta el tema específico brindado y el objetivo de aprendizaje, 
        se específico y dame una introducción de no más de un párrafo. 
        '''

        objetivos_prompt = '''
        Dame un listado de los cinco principales objetivos del proyecto, estos deben estar enmarcados en el tema específico 
        y cumplir los objetivos de aprendizaje.
        ''' 

        requisitos_prompt = '''
        Dame un listado de los cinco requisitos básicos de conocimiento que un estudiante debería de tener para poder realizar 
        el proyecto y cumplir los objetivos planteados, ten en cuenta que son estudiantes universitarios de la carrera señalada.  
        Dame el listado sin incluir observaciones finales.
        '''

        recursos_prompt = '''
        Dame un listado de los cinco recursos materiales básicos con que un estudiante debería de contar para poder realizar el 
        proyecto y cumplir los objetivos planteados, ten en cuenta que son estudiantes universitarios de la carrera señalada. 
        Dame el listado sin incluir observaciones finales.
        '''

        actividades_prompt = '''
        Dame un listado de las actividades que se deben desarrollar para cada una de las sesiones planteadas para el proyecto, 
        estas actividades deben ser especificadas para el docente y el estudiante. Las actividades señaladas deben buscar cumplir 
        el objetivo y temática planteada, enmarcadas en la metodología señalada. Se específico y sigue un curso lógico de sesiones
        y temáticas, teniendo en cuenta la cantidad de sesiones. Dame el listado sin incluir observaciones finales.
        '''

        evaluacion_prompt = '''
        Dame en un cuadro, en el cual los criterios de evaluación a los estudiantes se encuentran en el eje y en el x las notas 
        que puede obtener un estudiante (Excelente, Sobresaliente, Aceptable y Bajo), y en los cruces de los criterios de 
        evaluación y las notas, dame los criterios para establecer si un estudiante merece esa nota, deseo descripcions de esos criterios. Los criterios que se 
        especifican en el eje y, deben ser criterios asociados a la temática y objetivos específicos del proyecto, dame cinco 
        criterios.
        '''

        prompts = [intro_prompt, objetivos_prompt, requisitos_prompt, recursos_prompt, actividades_prompt, evaluacion_prompt]

        messages = [{'role' : 'system', 
                    'content' : preprompt}]


        for instrucciones in prompts:
            messages.append({'role' : 'user', 'content' : instrucciones})

            response = openai.ChatCompletion.create(
                model = 'gpt-3.5-turbo',
                messages = messages,
                temperature = 0.5
            )

            respuesta = response.choices[0].message.content

            messages.append({'role' : 'system', 'content' : respuesta})

        resp_intro = messages[2]['content']
        resp_objetivos = messages[4]['content']
        resp_requisitos = messages[6]['content']
        resp_recursos = messages[8]['content']
        resp_actividades = messages[10]['content']
        resp_evaluacion = messages[12]['content']

        st.markdown('## Introduccion')
        st.write(resp_intro)

        st.markdown('## Objetivos')
        st.write(resp_objetivos)

        st.markdown('## Requisitos')
        st.write(resp_requisitos)

        st.markdown('## Recursos')
        st.write(resp_recursos)

        st.markdown('## Actividades')
        st.write(resp_actividades)

        st.markdown('## Evaluacion')
        st.write(resp_evaluacion)
    
    st.success('Listo!')