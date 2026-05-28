import os

file_path = 'c:/Users/adrmu/Desktop/IA/Proyecto/IA-2526-Info-7/memoria/memoria.tex'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the listings package and its styling
header_to_remove = r"""\usepackage{listings}
\usepackage{xcolor}

% Colores para los listings de código
\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}
\lstset{style=mystyle}"""

content = content.replace(header_to_remove, "")

# Remove the code block and replace with text explanation
code_to_remove = r"""cuyo núcleo programático en lenguaje Python queda ilustrado concisamente en el siguiente \emph{snippet} de código, destacando la interacción ineludible con los procesos formales empíricos funcionales de la librería NLTK y Porter Stemmer:

\begin{lstlisting}[language=Python, caption=Implementación del Tokenizador Personalizado]
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

def tokenizador_pokemon(text):
    '''Tokeniza y extrae raices lexicas.'''
    tokens = word_tokenize(text)
    clean_tokens = [
        stemmer.stem(token.lower()) for token in tokens 
        if token.isalpha() and 
           token.lower() not in stop_words
    ]
    return clean_tokens

vectorizador = TfidfVectorizer(
    token_pattern=None,
    tokenizer=tokenizador_pokemon
)
tfidf_matrix = vectorizador.fit_transform(documents)
\end{lstlisting}"""

replacement_text = r"""cuyo núcleo metodológico se basa en un diseño imperativo secuencial de filtrado lingüístico. En este diseño, cada documento extraído iterativamente se segmenta en sus componentes atómicos fundamentales mediante un algoritmo estandarizado de división. Seguidamente, se ejecuta un sub-proceso heurístico que descarta de manera rigurosa y algorítmicamente implacable todos aquellos elementos que contengan caracteres no alfabéticos, depurando consecuentemente el corpus de signos de puntuación, delimitadores y numéricos. 

El filtro subsiguiente somete los elementos restantes a una validación estocástica negativa frente a un diccionario universal de \emph{stop-words} del idioma inglés (obtenido operativamente mediante la suite léxica NLTK), excluyendo artículos y preposiciones carentes de semántica. Finalmente, la lista de vocablos supervivientes es canalizada obligatoriamente a través del afamado algoritmo algorítmico \emph{Porter Stemmer}, el cual poda paramétricamente los sufijos flexivos morfológicos extrayendo iterativamente la raíz lexema inalterada. Esta secuencia finita de operaciones normalizadoras, integrada como parámetro directo al proceso general asintótico empírico TF-IDF paramétrico de \emph{scikit-learn}, consolida formal y computacionalmente la asombrosamente reducida dimensión cardinal absoluta del vocabulario final recuperable."""

content = content.replace(code_to_remove, replacement_text)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Code removed successfully.")
