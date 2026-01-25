#!/bin/bash

# 1. THE ROYAL (Classic Center Layout)
cat << 'INNER' > estate_royal.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Royal Estate</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap');
        body { background: #0a0a0a; color: #d4af37; font-family: 'Cinzel', serif; }
        .hero { height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; border: 20px solid #d4af37; margin: 20px; text-align: center; }
        .menu { writing-mode: vertical-rl; position: fixed; right: 40px; top: 50%; transform: translateY(-50%); letter-spacing: 5px; }
    </style>
</head>
<body>
    <div class="menu text-xs">COLLECTION — ABOUT — CONTACT</div>
    <div class="hero">
        <h1 class="text-7xl mb-4">ROYAL</h1>
        <p class="text-white tracking-[10px] text-sm">ESTABLISHED IN LONDON</p>
        <div class="mt-20 w-[1px] h-32 bg-[#d4af37]"></div>
    </div>
    <section class="p-20 grid grid-cols-1 gap-20">
        <div class="border-b border-[#d4af37] pb-10">
            <img src="https://images.unsplash.com/photo-1580587767303-9fef00803114?w=800" class="w-full h-[600px] object-cover mb-6">
            <h2 class="text-4xl">THE MANOR</h2>
        </div>
    </section>
</body>
</html>
INNER

# 2. THE URBAN (Asymmetric Grid Layout)
cat << 'INNER' > estate_urban.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Urban Core</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #f0f0f0; color: #111; font-family: 'Helvetica', sans-serif; }
        .grid-custom { display: grid; grid-template-columns: repeat(12, 1fr); gap: 10px; padding: 10px; }
    </style>
</head>
<body>
    <nav class="p-10 flex justify-between font-bold italic text-3xl">
        <div>URBAN_CORE</div>
        <div class="text-sm not-italic">NYC / 2026</div>
    </nav>
    <div class="grid-custom">
        <div class="col-span-8 bg-black h-[500px] text-white p-10 flex items-end">
            <h1 class="text-9xl font-black">LOFT.</h1>
        </div>
        <div class="col-span-4 bg-orange-600 h-[500px] p-10 text-white">
            <p>Modern investment apartments for the new generation.</p>
        </div>
        <div class="col-span-4 h-64 overflow-hidden">
            <img src="https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=500" class="w-full h-full object-cover">
        </div>
        <div class="col-span-8 border-4 border-black p-10 flex items-center justify-center">
            <button class="text-5xl font-black hover:bg-black hover:text-white p-4 transition">VIEW ALL UNITS -></button>
        </div>
    </div>
</body>
</html>
INNER

# 3. THE ECO (Clean Zen Layout)
cat << 'INNER' > estate_eco.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Eden Eco</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #fff; color: #2d4a22; }
        .circle-img { border-radius: 50% 50% 0 0; }
    </style>
</head>
<body>
    <div class="max-w-4xl mx-auto py-20 px-10">
        <header class="text-center mb-20">
            <div class="w-16 h-16 bg-[#2d4a22] rounded-full mx-auto mb-6"></div>
            <h1 class="text-4xl font-light tracking-widest italic">EDEN.</h1>
        </header>
        <div class="flex gap-10 items-center mb-32">
            <img src="https://images.unsplash.com/photo-1518780664697-55e3ad937233?w=500" class="w-1/2 circle-img">
            <div>
                <h2 class="text-3xl mb-4 italic">Breathe.</h2>
                <p class="text-gray-500 leading-loose">Homes built with nature, not against it. Sustainable materials, zero carbon footprint.</p>
            </div>
        </div>
    </div>
</body>
</html>
INNER

# 4. THE GLASS (Futuristic Dashboard Layout)
cat << 'INNER' > estate_glass.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><title>Horizon Glass</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #000; color: #00f2ff; font-family: 'Courier New', monospace; }
        .panel { border: 1px solid #00f2ff; background: rgba(0, 242, 255, 0.05); }
        .scanner { height: 2px; background: #00f2ff; width: 100%; position: relative; animation: scan 3s infinite linear; }
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }
    </style>
</head>
<body class="p-4 overflow-hidden h-screen flex flex-col">
    <div class="flex justify-between mb-4 panel p-2 text-xs">
        <span>SYSTEM: ONLINE</span>
        <span>LOCATION: NEON_CITY_LEVEL_88</span>
    </div>
    <div class="flex-grow grid grid-cols-12 gap-4">
        <div class="col-span-3 panel p-4 relative overflow-hidden">
            <div class="scanner"></div>
            <h2 class="mb-4">[DATA_LOG]</h2>
            <div class="text-[10px] opacity-50">
                Property_ID: 99x-A<br>Price: 1.2M CRD<br>Oxygen_Level: 98%
            </div>
        </div>
        <div class="col-span-6 panel relative">
            <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800" class="w-full h-full object-cover opacity-60">
            <div class="absolute inset-0 flex items-center justify-center">
                <h1 class="text-6xl font-bold tracking-tighter">FUTURE_LIVING</h1>
            </div>
        </div>
        <div class="col-span-3 panel p-4 flex flex-col justify-between">
            <button class="panel p-4 hover:bg-[#00f2ff] hover:text-black transition uppercase">Enter_Vault</button>
            <div class="text-[8px]">ARCHITECTURE V3.0.2</div>
        </div>
    </div>
</body>
</html>
INNER

bash generate_sites.sh
git add .
git commit -m "Titan Evolution: 4 Distinct Architectural Styles Deployed"
git push origin main --force
