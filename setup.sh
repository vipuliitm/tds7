mkdir -p ~/.streamlt/

echo "\n
[general]\n\
email = \'21f1005862@student.onlinedegree.iitm.ac.in'\n\
" > ~/.streamlit/credntials.toml

echo "\n
[server]\n\
headless= true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
