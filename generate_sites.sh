#!/bin/bash

# 1. THE ROYAL (Elegant Museum Style)
cat << 'INNER' > estate_royal.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Royal Estate | Legacy</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora&display=swap');
        body { background: #0c0c0c; color: #c5a059; font-family: 'Lora', serif; }
        h1 { font-family: 'Playfair Display', serif; letter-spacing: 0.2em; }
        .hero { height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle, #1a1a1a 0%, #000 100%); border: 1px solid #c5a059; margin: 30px; }
        .nav-royal { position: absolute; top: 60px; width: 100%; text-align: center; text-transform: uppercase; font-size: 10px; letter-spacing: 4px; }
    </style>
</head>
<body>
    <div class="nav-royal underline decoration-1">The Collection — Heritage — Global Offices</div>
    <div class="hero flex-col">
        <h1 class="text-6xl md:text-8xl mb-4">ROYAL</h1>
        <div class="h-[1px] w-24 bg-[#c5a059] mb-8"></div>
        <p class="text-white italic opacity-50">Estates for the Sovereigns</p>
        <button class="mt-12 border border-[#c5a059] px-10 py-3 hover:bg-[#c5a059] hover:text-black transition duration-700 uppercase text-[10px]">Private Entrance</button>
    </div>
</body>
</html>
INNER

# 2. THE URBAN (Sharp Commercial Grid)
cat << 'INNER' > estate_urban.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Urban Core | NYC</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@900&display=swap');
        body { background: #f4f4f4; color: #000; font-family: 'Inter', sans-serif; }
        .grid-box { border-bottom: 5px solid #000; border-right: 5px solid #000; }
    </style>
</head>
<body class="p-0 m-0">
    <div class="grid grid-cols-12 h-screen">
        <div class="col-span-12 md:col-span-8 bg-black p-12 flex flex-col justify-between">
            <h1 class="text-white text-[15vw] leading-none tracking-tighter">URBAN<br>CORE.</h1>
            <div class="text-orange-500 text-2xl">LATEST LISTINGS / 2026</div>
        </div>
        <div class="col-span-12 md:col-span-4 p-12 flex flex-col justify-between border-l-8 border-black">
            <p class="text-3xl font-bold italic leading-tight">High-yield real estate in the world's most aggressive markets.</p>
            <button class="bg-black text-white p-6 text-center hover:bg-orange-600 transition">INVEST NOW -></button>
        </div>
    </div>
</body>
</html>
INNER

# 3. THE ECO (Nature Zen Layout)
cat << 'INNER' > estate_eco.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Eden Eco | Harmony</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #fdfbf7; color: #354a21; }
        .leaf-shape { border-radius: 0 100px 0 100px; }
    </style>
</head>
<body class="flex items-center justify-center min-h-screen p-10">
    <div class="max-w-6xl w-full grid md:grid-cols-2 gap-20 items-center">
        <div class="order-2 md:order-1">
            <span class="text-sm tracking-[5px] font-bold opacity-60">SUSTAINABLE ARCHITECTURE</span>
            <h1 class="text-7xl font-serif mt-4 mb-8">Breathe<br>Living.</h1>
            <p class="text-lg leading-relaxed text-gray-600 mb-10">Experience villas designed to be a part of the ecosystem, utilizing solar intelligence and living materials.</p>
            <a href="#" class="underline font-bold hover:text-green-800 transition">View Forest Resorts</a>
        </div>
        <div class="order-1 md:order-2">
            <img src="https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=800" class="leaf-shape shadow-2xl">
        </div>
    </div>
</body>
</html>
INNER

# 4. THE GLASS (Cyber-Glass Interface)
cat << 'INNER' > estate_glass.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Horizon | Future Living</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #000; color: #0ff; font-family: monospace; overflow: hidden; }
        .glass-panel { background: rgba(0, 255, 255, 0.03); border: 1px solid rgba(0, 255, 255, 0.2); backdrop-filter: blur(10px); }
        .neon-line { height: 1px; background: linear-gradient(90deg, transparent, #0ff, transparent); }
    </style>
</head>
<body class="p-6 h-screen flex flex-col">
    <div class="flex justify-between mb-6 text-[10px]">
        <div>TITAN_CORE_OS_v3.0</div>
        <div class="animate-pulse">LATENCY: 12ms</div>
    </div>
    <div class="flex-grow flex gap-6">
        <div class="w-1/4 glass-panel p-6 flex flex-col justify-between">
            <div>
                <div class="text-xs mb-10">[ PROPERTY SCANNER ]</div>
                <div class="mb-4">SKY_UNIT_88</div>
                <div class="h-24 w-full bg-[#0ff]/10 mb-6"></div>
            </div>
            <div class="text-[9px] opacity-40">ENCRYPTED ASSET STORAGE</div>
        </div>
        <div class="w-3/4 glass-panel relative p-10">
            <div class="neon-line mb-10"></div>
            <h1 class="text-8xl font-black italic tracking-tighter opacity-80">HORIZON</h1>
            <p class="mt-10 max-w-md">Vertical cities. Smart glass. The evolution of human habitat.</p>
            <div class="absolute bottom-10 right-10 border border-[#0ff] p-6 hover:bg-[#0ff] hover:text-black cursor-pointer">INITIALIZE_PURCHASE</div>
        </div>
    </div>
</body>
</html>
INNER

bash generate_sites.sh
git add .
git commit -m "Titan Final Evolution: Unique Structural Diversity Deployed"
git push origin main --force
