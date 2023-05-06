import streamlit as st

st.set_page_config(layout='wide')
st.title("Introduction to the Gaming Industry")
tab1, tab2 = st.tabs(["Introduction", "About this App"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        image = 'images/Image1.jpg'
        st.image(image)
    with col2:
        st.markdown("The gaming industry refers to the business of creating, designing, producing, publishing, and distributing video games. Video games have become a popular form of entertainment around the world and have evolved over the years from simple, pixelated games to complex, immersive experiences that often rival movies and television shows in terms of production value and storytelling.")
    
    st.markdown("The gaming industry includes a variety of companies, including:")
    st.markdown(" - Game developers, who create the games themselves")
    st.markdown(" - Publishers, who handle the marketing, distribution, and sales of the games")
    st.markdown(" - Hardware manufacturers, who produce the consoles and devices that gamers use to play the games")
    st.markdown(" - Retailers, who sell the games and hardware to consumers")
    st.markdown("The gaming industry is a rapidly growing and lucrative industry, with revenue reaching billions of dollars each year. It is also a highly competitive industry, with many developers and publishers vying for the attention and loyalty of gamers.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Some of the most popular game genres include:")
        st.markdown(" - Action Adventure")
        st.markdown(" - Role-playing")
        st.markdown(" - Sports")
        st.markdown(" - Racing")
        st.markdown(" - Simulation")
        st.markdown("Games can be played on a variety of platforms, including consoles, computers, mobile devices, and virtual reality devices.")
    with col2:
        image = 'images/Image2.jpg'
        st.image(image)

with tab2:
    st.write("This app provides us insights into the latest consoles in the market today, namely, PS5, XBox Series X and NS. We also take a closer look at the top rated games, sales and ratings across all platforms.")
    st.header("About the Data")
    st.write("For the latest console data we look at Amazon reviews")
    st.write("For the top rated games and sales data we will use vgchartz.com as our source")

    st.subheader("Data Sources:")
    PS5 = '[PS5 Amazon Reviews](https://www.amazon.com/PlayStation-5-Console/product-reviews/B08FC5L3RG/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=)'
    Xbox = '[Xbox Series X Amazon Reviews](https://www.amazon.com/portal/customer-reviews/B08H75RTZ8/ref=cm_cr_dp_mb_top)'
    NS = '[Nintendo Switch Amazon Reviews](https://www.amazon.com/portal/customer-reviews/B098RL6SBJ/ref=cm_cr_dp_mb_top)'
    VG = '[vgchartz](https://www.vgchartz.com/)'
    st.markdown(PS5,unsafe_allow_html=True)
    st.markdown(Xbox,unsafe_allow_html=True)
    st.markdown(NS,unsafe_allow_html=True)
    st.markdown(VG,unsafe_allow_html=True)

    st.subheader('Image Sources:')
    st.markdown('https://cdn.dribbble.com/users/761988/screenshots/2510880/giffas_pacman.gif')
    st.markdown('https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/tmt/ey-hand-holding-video-game-controller-city-night-background.jpg')
    st.markdown('https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/tmt/ey-hand-holding-video-game-controller-city-night-background.jpg')
    st.markdown('https://assets.ey.com/content/dam/ey-sites/ey-com/en_gl/topics/tmt/ey-hand-holding-video-game-controller-city-night-background.jpg')
    st.markdown('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJ00g8k4bHt5n9fOnC7c0CFXqRA4aJcXpdA5_KSkIE9xiw4kUs')
    st.markdown('https://cdn.wallpapersafari.com/47/67/AM6rKQ.png')