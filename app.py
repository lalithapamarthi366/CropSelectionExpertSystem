import streamlit as st

from knowledge_base import (
    SOIL_TYPES,
    SEASONS,
    WATER_LEVELS,
    RAINFALL_LEVELS,
    TEMPERATURE_LEVELS,
    IRRIGATION_LEVELS,
    MOISTURE_LEVELS,
    FARM_SIZES,
    PREVIOUS_CROPS,
    GOALS
)

from inference_engine import get_recommendation


# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Crop Selection Expert System",
    page_icon="🌱",
    layout="centered"
)


# ---------------- WHITE & GREEN THEME ----------------

st.markdown("""
<style>

.stApp {
    background-color: white;
}

/* Main Title */
.main-title {
    color: #16803a !important;
    text-align: center;
    font-size: 38px;
    font-weight: bold;
}

/* Subtitle */
.subtitle {
    color: black !important;
    text-align: center;
    font-size: 17px;
    margin-bottom: 25px;
}

/* Section Headings */
.section-title {
    color: #16803a !important;
    font-size: 24px;
    font-weight: bold;
}

/* Normal Text */
p {
    color: black !important;
}

label {
    color: black !important;
}

.stMarkdown {
    color: black !important;
}

/* Selectbox */
div[data-baseweb="select"] {
    color: black !important;
}

div[data-baseweb="select"] * {
    color: black !important;
}

/* Selectbox Dropdown */
ul[role="listbox"] {
    background-color: white !important;
}

ul[role="listbox"] li {
    color: black !important;
}

/* Button */
div.stButton > button {
    background-color: #16803a;
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 10px;
    font-size: 17px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #0f662e;
    color: white !important;
}

/* Recommendation Box */
.recommendation {
    background-color: #e8f8e8;
    border-left: 6px solid #16803a;
    padding: 18px;
    border-radius: 10px;
    margin-top: 20px;
}

.recommendation h2 {
    color: #16803a !important;
}

.recommendation p {
    color: black !important;
}

/* Subheadings */
h2, h3 {
    color: #16803a !important;
}

/* Rule Box */
pre {
    background-color: #f5f5f5 !important;
    color: black !important;
}

code {
    color: black !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #555555 !important;
    font-size: 13px;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🌱 Crop Selection Expert System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Smart crop recommendation using Rule-Based Artificial Intelligence'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- FARM DETAILS ----------------

st.markdown(
    '<div class="section-title">🌾 Enter Your Farm Details</div>',
    unsafe_allow_html=True
)

st.write("Answer the following questions:")


soil = st.selectbox(
    "1️⃣ Soil Type",
    SOIL_TYPES
)

season = st.selectbox(
    "2️⃣ Season",
    SEASONS
)

water = st.selectbox(
    "3️⃣ Water Availability",
    WATER_LEVELS
)

rainfall = st.selectbox(
    "4️⃣ Rainfall Level",
    RAINFALL_LEVELS
)

temperature = st.selectbox(
    "5️⃣ Temperature",
    TEMPERATURE_LEVELS
)

irrigation = st.selectbox(
    "6️⃣ Irrigation Facility",
    IRRIGATION_LEVELS
)

moisture = st.selectbox(
    "7️⃣ Soil Moisture",
    MOISTURE_LEVELS
)

farm_size = st.selectbox(
    "8️⃣ Farm Size",
    FARM_SIZES
)

previous_crop = st.selectbox(
    "9️⃣ Previous Crop",
    PREVIOUS_CROPS
)

goal = st.selectbox(
    "🔟 Farmer's Main Goal",
    GOALS
)


st.divider()


# ---------------- RECOMMENDATION BUTTON ----------------

if st.button(
    "🌱 Get Crop Recommendation",
    use_container_width=True
):

    user_input = {
        "soil": soil,
        "season": season,
        "water": water,
        "rainfall": rainfall,
        "temperature": temperature,
        "irrigation": irrigation,
        "moisture": moisture,
        "farm_size": farm_size,
        "previous_crop": previous_crop,
        "goal": goal
    }


    # Get result from inference engine
    result = get_recommendation(user_input)


    # ---------------- RESULT ----------------

    st.markdown(
        '<div class="section-title">🌾 Recommendation</div>',
        unsafe_allow_html=True
    )


    # ---------------- NO STRONG RECOMMENDATION ----------------

    if result["crop"] == "No strong recommendation":

        st.warning(
            "⚠️ No strong crop recommendation found."
        )

        st.info(
            f"Rule Match Score: {result['score']}"
        )

        st.write(
            "Try selecting different farm conditions "
            "that better match the available rules."
        )


    # ---------------- CROP RECOMMENDATION ----------------

    else:

        st.markdown(
            f"""
            <div class="recommendation">
                <h2>🌱 Recommended Crop: {result['crop']}</h2>
                <p><b>Rule Match Score:</b> {result['score']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


        # ---------------- MATCHING CONDITIONS ----------------

        st.write("")

        st.subheader("🧠 Matching Conditions")

        for match in result["matches"]:
            st.write("✅", match)


        # ---------------- RULE USED ----------------

        st.subheader("📋 Rule Applied")

        rule = result["rule"]

        st.code(
            f"IF Soil = {rule['soil']}\n"
            f"AND Season = {rule['season']}\n"
            f"AND Water = {rule['water']}\n"
            f"AND Rainfall = {rule['rainfall']}\n"
            f"AND Temperature = {rule['temperature']}\n"
            f"AND Irrigation = {rule['irrigation']}\n"
            f"AND Soil Moisture = {rule['moisture']}\n"
            f"AND Farm Size = {rule['farm_size']}\n"
            f"AND Previous Crop = {rule['previous_crop']}\n"
            f"AND Goal = {rule['goal']}\n"
            f"THEN Crop = {rule['crop']}"
        )


# ---------------- FOOTER ----------------

st.markdown(
    '<div class="footer">'
    '🌿 Educational Rule-Based Expert System • Crop Selection Project'
    '</div>',
    unsafe_allow_html=True
)