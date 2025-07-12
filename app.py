import streamlit as st
import streamlit_shadcn_ui as ui

# Set page config
st.set_page_config(
    page_title="Streamlit ShadCN UI Demo",
    page_icon="🎨",
    layout="wide"
)

# Main title
st.title("🎨 Streamlit ShadCN UI Components Demo")
st.markdown("This demo showcases ShadCN UI components integrated with Streamlit.")

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    st.header("Buttons")
    
    # Button components
    if ui.button("Primary Button", key="btn1"):
        st.success("Primary button clicked!")
    
    if ui.button("Secondary Button", key="btn2", variant="secondary"):
        st.info("Secondary button clicked!")
    
    st.header("Input Components")
    
    # Input component
    user_input = ui.input(placeholder="Enter your name...", key="input1")
    if user_input:
        st.write(f"Hello, {user_input}!")
    
    # Textarea component
    text_area_value = ui.textarea(
        placeholder="Tell us about yourself...",
        key="textarea1"
    )
    if text_area_value:
        st.write(f"You wrote: {text_area_value}")

with col2:
    st.header("Selection Components")
    
    # Select component
    selected_option = ui.select(
        options=["Red", "Blue", "Green", "Yellow", "Purple"],
        key="select1"
    )
    if selected_option:
        st.write(f"You selected: {selected_option}")
    
    # Switch component
    switch_value = ui.switch(key="switch1")
    st.write(f"Switch is: {'ON' if switch_value else 'OFF'}")
    
    # Checkbox component
    checkbox_value = ui.checkbox("I agree to the terms", key="checkbox1")
    st.write(f"Terms accepted: {checkbox_value}")

# Full width components
st.header("Card Component")

# Card component
with ui.card(key="card1"):
    st.subheader("Welcome Card")
    st.write("This is a beautiful card component from ShadCN UI.")
    st.write("It can contain any Streamlit content!")
    
    # Progress bar inside card
    progress_value = 75
    st.progress(progress_value / 100)
    st.write(f"Progress: {progress_value}%")

# Tabs component
st.header("Tabs Component")

tab_value = ui.tabs(options=["Tab 1", "Tab 2", "Tab 3"], key="tabs1")

if tab_value == "Tab 1":
    st.write("**Content for Tab 1**")
    st.info("This is the first tab content with ShadCN styling.")
elif tab_value == "Tab 2":
    st.write("**Content for Tab 2**")
    st.warning("This is the second tab content with ShadCN styling.")
elif tab_value == "Tab 3":
    st.write("**Content for Tab 3**")
    st.success("This is the third tab content with ShadCN styling.")

# Date Picker
st.header("Date Picker")

selected_date = ui.date_picker(key="date1")
if selected_date:
    st.write(f"Selected date: {selected_date}")

# Avatar component
st.header("Avatar Component")

ui.avatar("https://github.com/shadcn.png", key="avatar1")

# Separator
st.markdown("---")

# Footer
st.markdown(
    """
    <div style='text-align: center; color: #666; margin-top: 2rem;'>
        <p>Built with ❤️ using Streamlit and ShadCN UI</p>
        <p>This demo shows the integration of modern UI components with Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)