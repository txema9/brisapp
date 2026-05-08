import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BRISA",
    page_icon="🌊",
    layout="wide"
)

html = """

<!DOCTYPE html>
<html>

<head>

<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<link rel="stylesheet"
href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>

<script
src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js">
</script>

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:sans-serif;
}

body{

    background:#081120;

    display:flex;

    justify-content:center;

    align-items:center;

    height:100vh;

    overflow:hidden;
}

.phone{

    width:390px;
    height:844px;

    border-radius:42px;

    overflow:hidden;

    position:relative;

    background:#000;

    border:10px solid #111827;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.45);
}

#map{

    position:absolute;
    inset:0;
    z-index:1;
}

/* LOGO */

.logo{

    position:absolute;

    top:56px;
    left:20px;

    z-index:1200;

    color:white;
}

.logo-title{

    font-size:34px;
    font-weight:700;

    display:flex;
    align-items:center;
}

.logo-sub{

    margin-top:4px;

    font-size:13px;

    color:rgba(255,255,255,0.72);
}

.live-dot{

    display:inline-block;

    width:12px;
    height:12px;

    margin-left:10px;

    border-radius:50%;

    background:#ef4444;

    box-shadow:
        0 0 12px rgba(239,68,68,0.9);

    animation:
        pulseLive 1.2s infinite;
}

@keyframes pulseLive{

    0%{
        transform:scale(1);
        opacity:1;
    }

    50%{
        transform:scale(1.35);
        opacity:0.45;
    }

    100%{
        transform:scale(1);
        opacity:1;
    }
}

/* SEARCH */

.search-wrapper{

    position:absolute;

    top:54px;
    right:18px;

    z-index:1200;
}

.search-container{

    width:52px;
    height:52px;

    border-radius:999px;

    background:
        rgba(245,245,245,0.82);

    backdrop-filter:
        blur(20px);

    display:flex;

    align-items:center;

    overflow:hidden;

    transition:0.35s ease;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.18);
}

.search-container.active{

    width:260px;
}

.search-icon{

    width:52px;
    min-width:52px;

    height:52px;

    display:flex;

    align-items:center;
    justify-content:center;

    color:#111827;

    cursor:pointer;

    font-size:15px;
}

.search-input{

    flex:1;

    background:none;

    border:none;

    outline:none;

    color:#111827;

    font-size:15px;

    opacity:0;

    transition:0.25s ease;
}

.search-container.active .search-input{

    opacity:1;
}

.search-input::placeholder{

    color:rgba(17,24,39,0.45);
}

/* SHEET */

.sheet{

    position:absolute;

    left:0;
    bottom:0;

    width:100%;
    height:52%;

    background:
        rgba(245,245,245,0.80);

    backdrop-filter:
        blur(30px);

    border-top-left-radius:34px;
    border-top-right-radius:34px;

    padding:18px 18px 110px 18px;

    z-index:999;

    transition:
        height 0.15s ease;
}

.handle{

    width:58px;
    height:6px;

    border-radius:999px;

    background:rgba(0,0,0,0.18);

    margin:0 auto 18px auto;

    cursor:pointer;

    touch-action:none;
}

.content{

    overflow-y:auto;

    height:100%;

    padding-bottom:160px;
}

.content::-webkit-scrollbar{
    width:0px;
}

/* TITLES */

.sheet-title{

    font-size:30px;
    font-weight:700;

    color:#111827;

    margin-bottom:18px;
}

/* ZONES */

.zone-item{

    background:
        rgba(255,255,255,0.52);

    border:
        1px solid rgba(255,255,255,0.35);

    border-radius:
        22px;

    padding:
        18px;

    margin-bottom:
        14px;

    cursor:pointer;

    transition:0.25s;
}

.zone-item.active{

    border:
        2px solid #60a5fa;

    background:
        rgba(255,255,255,0.92);
}

.zone-title{

    font-size:20px;
    font-weight:700;

    color:#111827;
}

.zone-desc{

    margin-top:5px;

    font-size:14px;

    color:#4b5563;
}

.zone-moods{

    display:flex;

    flex-wrap:nowrap;

    overflow-x:auto;

    gap:8px;

    margin-top:14px;
}

.zone-moods::-webkit-scrollbar{
    display:none;
}

.mood{

    background:
        rgba(255,255,255,0.72);

    padding:
        7px 11px;

    border-radius:
        999px;

    font-size:12px;

    font-weight:600;

    color:#111827;

    white-space:nowrap;

    flex-shrink:0;
}

/* NAV */

.bottom-nav{

    position:absolute;

    bottom:14px;
    left:50%;

    transform:translateX(-50%);

    width:90%;

    height:68px;

    background:
        rgba(20,20,20,0.82);

    backdrop-filter:
        blur(25px);

    border-radius:
        24px;

    display:flex;

    justify-content:space-around;

    align-items:center;

    color:white;

    z-index:1001;
}

.nav-item{

    display:flex;

    flex-direction:column;

    align-items:center;

    font-size:11px;

    opacity:0.7;

    cursor:pointer;
}

.nav-item.active{
    opacity:1;
}

.nav-item i{

    font-size:20px;

    margin-bottom:5px;
}

/* PIN */

.pin-wrapper{

    position:relative;

    width:34px;
    height:46px;
}

.pin{

    width:34px;
    height:34px;

    background:#111827;

    border-radius:
        50% 50% 50% 0;

    transform:
        rotate(-45deg);

    position:absolute;

    top:0;
    left:0;

    box-shadow:
        0 0 18px rgba(96,165,250,0.45);
}

.pin::after{

    content:"";

    width:14px;
    height:14px;

    background:#1e3a8a;

    border-radius:50%;

    position:absolute;

    top:10px;
    left:10px;
}

.pin-emoji{

    position:absolute;

    top:5px;
    left:5px;

    width:24px;
    height:24px;

    display:flex;

    align-items:center;
    justify-content:center;

    font-size:14px;

    z-index:10;
}

/* DISCOVER */

.discover-card{

    background:
        rgba(255,255,255,0.52);

    border-radius:
        26px;

    padding:
        22px;
}

/* PROFILE */

.login-box{

    background:
        rgba(255,255,255,0.52);

    border-radius:
        26px;

    padding:
        22px;
}

.input{

    width:100%;

    padding:15px;

    border:none;

    border-radius:14px;

    margin-bottom:14px;

    font-size:15px;
}

.button{

    width:100%;

    padding:15px;

    border:none;

    border-radius:16px;

    background:#111827;

    color:white;

    font-weight:700;

    cursor:pointer;
}

</style>

</head>

<body>

<div class="phone">

    <div id="map"></div>

    <div class="logo">

        <div class="logo-title">
            BRISA
            <span class="live-dot"></span>
        </div>

        <div class="logo-sub">
            Santander en tiempo real
        </div>

    </div>

    <div class="search-wrapper">

        <div class="search-container"
             id="searchContainer">

            <div class="search-icon"
                 onclick="toggleSearch()">

                <i class="fa-solid fa-magnifying-glass"></i>

            </div>

            <input
                type="text"
                id="searchInput"
                class="search-input"
                placeholder="Buscar zona..."
                onkeyup="searchZone()">

        </div>

    </div>

    <div class="sheet"
         id="sheet">

        <div class="handle"
             id="handle">
        </div>

        <div class="content"
             id="content">
        </div>

    </div>

    <div class="bottom-nav">

        <div class="nav-item active"
             id="listaNav"
             onclick="showMap(this)">
            <i class="fa-solid fa-list"></i>
            <span>Lista</span>
        </div>

        <div class="nav-item"
             onclick="showDiscover(this)">
            <i class="fa-solid fa-compass"></i>
            <span>Descubre</span>
        </div>

        <div class="nav-item"
             onclick="showProfile(this)">
            <i class="fa-solid fa-user"></i>
            <span>Perfil</span>
        </div>

    </div>

</div>

<script>

var map = L.map('map', {
    zoomControl:false
}).setView([43.4623, -3.8099], 13);

L.tileLayer(
'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
{
    attribution:''
}).addTo(map);

const zones = [

{
name:"El Sardinero",
coords:[43.47234934934887,-3.7826310695260883],
marker:"🌊",
desc:"Playas y paseo marítimo",
moods:["🍴 Restauración","☀️ agradable","🚶 fluido"]
},

{
name:"Valdenoja",
coords:[43.4722,-3.7995],
marker:"🏡",
desc:"Barrio moderno y residencial",
moods:["🌫 sereno","🚶 fluido","🌊 agradable"]
}

];

let activeCircle = null;

function renderMapContent(filteredZones = zones){

    const content =
        document.getElementById("content");

    let html =
    `<div class="sheet-title">
        Áreas de Santander
    </div>`;

    filteredZones.forEach((z)=>{

        const realIndex =
            zones.indexOf(z);

        html += `

        <div class="zone-item"
             id="zone-${realIndex}"
             onclick="focusZone(${realIndex})">

            <div class="zone-title">
                ${z.name}
            </div>

            <div class="zone-desc">
                ${z.desc}
            </div>

            <div class="zone-moods">

                ${z.moods.map(m =>
                    `<div class="mood">${m}</div>`
                ).join("")}

            </div>

        </div>

        `;
    });

    content.innerHTML = html;
}

renderMapContent();

zones.forEach((z, index) => {

    const icon = L.divIcon({
        className:"",
        html:`
        <div class="pin-wrapper">

            <div class="pin"></div>

            <div class="pin-emoji">
                ${z.marker}
            </div>

        </div>
        `,
        iconSize:[34,46],
        iconAnchor:[17,46]
    });

    const marker = L.marker(
        z.coords,
        {icon:icon}
    ).addTo(map);

    marker.on("click", () => {

        document
            .getElementById("listaNav")
            .click();

        focusZone(index);

    });

});

function toggleSearch(){

    const container =
        document.getElementById("searchContainer");

    container.classList.toggle("active");

    if(container.classList.contains("active")){

        setTimeout(() => {

            document
                .getElementById("searchInput")
                .focus();

        }, 200);
    }
}

function searchZone(){

    const value =
        document.getElementById("searchInput")
        .value
        .toLowerCase();

    const filtered =
        zones.filter(z =>
            z.name.toLowerCase().includes(value)
        );

    renderMapContent(filtered);
}

function focusZone(index){

    const z = zones[index];

    map.setView(z.coords, 15);

    if(activeCircle){
        map.removeLayer(activeCircle);
    }

    activeCircle = L.circle(
        z.coords,
        {
            radius:230,
            color:"#60a5fa",
            fillColor:"#60a5fa",
            fillOpacity:0.18,
            weight:2
        }
    ).addTo(map);

    const items =
        document.querySelectorAll(".zone-item");

    items.forEach(i =>
        i.classList.remove("active")
    );

    const selected =
        document.getElementById(`zone-${index}`);

    if(selected){

        selected.classList.add("active");

        selected.scrollIntoView({
            behavior:"smooth",
            block:"center"
        });
    }
}

function showDiscover(nav){

    activateNav(nav);

    const random =
        zones[Math.floor(
            Math.random()*zones.length
        )];

    document.getElementById("content")
    .innerHTML = `

    <div class="sheet-title">
        Descubre
    </div>

    <div class="discover-card">

        <div style="
            font-size:30px;
            font-weight:700;
            color:#111827;
        ">
            ${random.marker} ${random.name}
        </div>

        <div style="
            margin-top:14px;
            color:#4b5563;
            line-height:1.5;
        ">
            Hoy BRISA recomienda esta zona
            por su equilibrio entre actividad,
            ambiente y movimiento urbano.
        </div>

        <div class="zone-moods"
             style="margin-top:18px;">

            ${random.moods.map(m =>
                `<div class="mood">${m}</div>`
            ).join("")}

        </div>

    </div>

    `;
}

function showProfile(nav){

    activateNav(nav);

    document.getElementById("content")
    .innerHTML = `

    <div class="sheet-title">
        Perfil
    </div>

    <div class="login-box">

        <input
            class="input"
            placeholder="Email">

        <input
            class="input"
            type="password"
            placeholder="Password">

        <button class="button">
            Iniciar sesión
        </button>

    </div>

    `;
}

function showMap(nav){

    activateNav(nav);

    renderMapContent();
}

function activateNav(nav){

    const navs =
        document.querySelectorAll(".nav-item");

    navs.forEach(n =>
        n.classList.remove("active")
    );

    nav.classList.add("active");
}

const sheet =
    document.getElementById("sheet");

const handle =
    document.getElementById("handle");

let startY = 0;
let currentHeight = 52;

sheet.style.height = currentHeight + "%";

handle.addEventListener("touchstart", (e) => {

    startY = e.touches[0].clientY;

});

handle.addEventListener("touchmove", (e) => {

    const currentY = e.touches[0].clientY;

    const diff = startY - currentY;

    let newHeight = currentHeight + (diff / 8);

    if(newHeight < 14){
        newHeight = 14;
    }

    if(newHeight > 82){
        newHeight = 82;
    }

    sheet.style.height = newHeight + "%";

});

handle.addEventListener("touchend", () => {

    currentHeight =
        parseFloat(sheet.style.height);

});

</script>

</body>
</html>

"""

components.html(
    html,
    height=900,
    scrolling=False
)