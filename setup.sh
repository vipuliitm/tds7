mkdir -p ~/.streamlit/  

echo "\
[general]\n\
email = \"21f1005862@student.onlinedegree.iitm.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless= true\n\
enableCORS=true\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
