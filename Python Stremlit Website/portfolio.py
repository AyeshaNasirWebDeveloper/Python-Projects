import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Digital Marketing Agency",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load images
service1_img = Image.open("Content/SEO.jpg") 
service2_img = Image.open("Content/SMM.jpg")
service3_img = Image.open("Content/Ad.jpg")

def main():
    # Hero Section
    st.markdown("""
    <style>
    .hero-image {
        height: 100vh; 
        width: 100%;
        object-fit: cover;
    }
    @media (max-width: 768px) {
        .hero-text h1 {
            font-size: 1.5rem !important; 
        }
        .hero-text p {
            font-size: 1rem !important;
        }
        .hero-text a {
            font-size: 0.6rem !important;        
        }
    }
    </style>
    """, unsafe_allow_html=True)


# Header Section
    st.markdown("""
    <style>
    .header {
        background-color: #000000;
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    .header a {
        color: white;
        text-decoration: none;
        margin: 0 15px;
        font-size: 1.2rem;
    }
    .header a:hover {
        color: #3498db;
    }
    .header .logo {
        font-size: 1.5rem;
        font-weight: bold;
        color: white;
    }
    @media (max-width: 768px) {
        .header {
            flex-direction: column;
            align-items: center;
            padding: 10px;
        }
        .header a {
            margin: 10px 3px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="header">
        <div class="logo">Marketing Agency</div>
        <div>
            <a href="#home">Home</a>
            <a href="#services">Services</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Hero Section
    st.markdown("""
    <div style="position: relative;">
        <img src="https://wallpapercg.com/media/ts_orig/8710.webp" class="hero-image"> 
        <div class="hero-text" style="text-align: center; color: white; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
            <h1 style="font-size: 3rem;">Transform Your Business with Our Digital Marketing Solutions</h1>
            <p style="font-size: 1.5rem;">We help brands grow with data-driven strategies, creative campaigns, and cutting-edge technology.</p>
            <a href="#services" style="background-color: #000000; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-size: 1.2rem;">Explore Our Services</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Services Section
    st.markdown("---")
    st.header("Our Services", anchor="services")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(service1_img, use_column_width=True)
        st.subheader("SEO & Content Marketing")
        st.write("Boost your online visibility with our proven SEO strategies and high-quality content.")
    with col2:
        st.image(service2_img, use_column_width=True)
        st.subheader("Social Media Management")
        st.write("Engage your audience and grow your brand with our social media expertise.")
    with col3:
        st.image(service3_img, use_column_width=True)
        st.subheader("Paid Advertising")
        st.write("Maximize ROI with targeted PPC campaigns and data-driven ad strategies.")

    # Testimonials Section
    st.markdown("---")
    st.header("What Our Clients Say")
    testimonial1, testimonial2, testimonial3 = st.columns(3)
    with testimonial1:
        st.markdown("""
        <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); text-align: center; margin-bottom: 2em;">
            <p style="font-style: italic;">"This agency transformed our business! Their strategies are top-notch."</p>
            <p style="font-weight: bold; color: #3498db;">- John Doe, CEO</p>
        </div>
        """, unsafe_allow_html=True)
    with testimonial2:
        st.markdown("""
        <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); text-align: center; margin-bottom: 2em;">
            <p style="font-style: italic;">"Highly professional team with a focus on results. Highly recommended!"</p>
            <p style="font-weight: bold; color: #3498db;">- Jane Smith, Marketing Head</p>
        </div>
        """, unsafe_allow_html=True)
    with testimonial3:
        st.markdown("""
        <div style="background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); text-align: center; margin-bottom: 2em;">
            <p style="font-style: italic;">"Their campaigns helped us achieve record-breaking sales."</p>
            <p style="font-weight: bold; color: #3498db;">- Mike Johnson, Founder</p>
        </div>
        """, unsafe_allow_html=True)

    # Contact Section
    st.markdown("---")
    st.header("Get in Touch")
    st.write("Ready to take your business to the next level? Let's talk!")
    contact_form = """
    <form action="https://formsubmit.co/your-email@example.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 100%; margin-bottom: 10px;">
        <input type="email" name="email" placeholder="Your Email" required style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 100%; margin-bottom: 10px;">
        <textarea name="message" placeholder="Your Message" required style="padding: 10px; border: 1px solid #ccc; border-radius: 5px; width: 100%; margin-bottom: 10px;"></textarea>
        <button type="submit" style="background-color: #000000; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer; width: 100%;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Footer Section
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #000000; color: white;">
        <p>Created by ❤️ <strong>Ayesha Nasir</strong></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()