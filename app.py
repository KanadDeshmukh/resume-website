import streamlit as st

# Title and subtitle
st.title("Your Name")
st.subheader("Software Developer | Wildlife Photographer | Marathon Enthusiast")

# About section
st.write("""
Hi, I'm [Your Name], a passionate software developer with a knack for building efficient and scalable applications. 
Apart from coding, I enjoy wildlife photography, bird watching, and training for long-distance marathons. 
I'm always open to exciting collaborations and learning opportunities.
""")

# Contact section with clickable links
st.write("### Contact Me")
st.write("[LinkedIn](https://www.linkedin.com/in/your-linkedin-url)")
st.write("[GitHub](https://github.com/your-github-username)")
st.write("[This Website](https://your-website-url.com)")

# Add an image (optional, can use a placeholder if you don't have one yet)
st.image("https://via.placeholder.com/300", caption="This could be your profile picture", use_column_width=True)

# Footer
st.write("© 2024 Your Name | All Rights Reserved")
