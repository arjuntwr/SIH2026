"""
================================================================================
Bhumi-Niti (भूमि-नीति): Automated Multimedia Video Production Pipeline
Zero-Touch Automation: Playwright Browser Choreography + Edge-TTS + FFmpeg
Smart India Hackathon 2026 | Problem Statement 26019 | Ministry of Rural Development
================================================================================
"""

import os
import sys
import time
import json
import asyncio
import subprocess
import urllib.request
from pathlib import Path

# Ensure console supports UTF-8
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# ------------------------------------------------------------------------------
# 0. CONFIGURATION & CONSTANTS
# ------------------------------------------------------------------------------
BASE_URL = "http://localhost:8000"
VOICE_NAME = "en-IN-PrabhatNeural"
OUTPUT_VIDEO = "bhumi_niti_platform_walkthrough.mp4"
TEMP_DIR = Path("build_demo_assets")
FPS = 60
WIDTH = 1920
HEIGHT = 1080

# ANSI Color Codes for Rich Terminal Output
C_RESET = "\033[0m"
C_BOLD = "\033[1m"
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_BLUE = "\033[94m"
C_MAGENTA = "\033[95m"
C_RED = "\033[91m"

def log_step(step: str, title: str):
    print(f"\n{C_BOLD}{C_CYAN}{step}{C_RESET} {C_BOLD}{title}{C_RESET}")

def log_info(msg: str):
    print(f"  {C_BLUE}ℹ{C_RESET} {msg}")

def log_success(msg: str):
    print(f"  {C_GREEN}✓{C_RESET} {msg}")

def log_warn(msg: str):
    print(f"  {C_YELLOW}⚠{C_RESET} {msg}")

def log_error(msg: str):
    print(f"  {C_RED}✗ {msg}{C_RESET}")

# ------------------------------------------------------------------------------
# 1. SCENE DEFINITIONS (FROM VIDEO_SCRIPT_STORYBOARD.md)
# ------------------------------------------------------------------------------
SCENES = [
    {
        "id": 1,
        "title": "The Land Governance Challenge",
        "lower_third": "PROBLEM STATEMENT 26019: EVIDENCE-BASED LAND GOVERNANCE | DoLR, MoRD",
        "script": (
            "Land is India's most critical economic asset, yet land governance has long been "
            "constrained by fragmented cadastral maps, static record-keeping, and disconnected legal archives. "
            "Under Ministry of Rural Development Problem Statement 26019, we present Bhumi-Niti: "
            "the National Digital Platform for Evidence-Based Land Governance. "
            "Engineered to strict GIGW 3.0 standards, Bhumi-Niti transforms raw land records into live, "
            "multi-dimensional spatial, environmental, and statutory intelligence."
        ),
    },
    {
        "id": 2,
        "title": "Real-Time Dynamic Search & Thematic Spotlight",
        "lower_third": "ZERO-LATENCY SEARCH & DYNAMIC SPOTLIGHT BOUNDARY | Shapely EPSG:7755",
        "script": (
            "The platform eliminates hardcoded demo pins. An administrator or researcher can search "
            "any village, taluka, PIN code, or industrial estate in Gujarat. "
            "Searching for 'Sanand' triggers instant reverse-geocoding and automated spatial polygon synthesis. "
            "The map dynamically executes a smooth vector fly-to, casting an illuminated cyan spotlight over the true "
            "revenue boundary while dimming extraneous territory. Every boundary coordinate is calculated on-the-fly "
            "using projected equal-area geometry, ensuring zero spatial distortion."
        ),
    },
    {
        "id": 3,
        "title": "Satellite-Calibrated 10m Sentinel-2 LULC Engine",
        "lower_third": "SENTINEL-2 10M LAND COVER ENGINE | Esri World Imagery & ESA Copernicus",
        "script": (
            "Rather than relying on coarse, outdated land classifications, Bhumi-Niti integrates "
            "the Sentinel-2 10-meter Land Cover engine, served directly via high-throughput raster tiles. "
            "With a single toggle, officials can switch between dark cartographic base layers and satellite imagery, "
            "fine-tuning raster opacity with precision sliders. The multi-spectral classification clearly isolates "
            "expanding built-up settlements in red, rich agrarian crop belts in yellow, and critical irrigation arteries "
            "in cyan—empowering district collectors to detect illegal encroachment and monitor agricultural land preservation in real time."
        ),
    },
    {
        "id": 4,
        "title": "Live Telemetry Dossier & Judicial Dispute Signals",
        "lower_third": "ETHICAL NON-PII TELEMETRY DOSSIER | NJDG eCourts & Soil Taxonomy",
        "script": (
            "On the right, the Live Intelligence Dossier streams synthesized telemetry computed specifically "
            "for the active polygon. Dynamic KPI cards instantly calculate total surface area, soil taxonomy, "
            "groundwater vulnerability, and municipal planning jurisdictions. "
            "Crucially, Bhumi-Niti adheres to strict data protection standards: zero citizen personal data is stored or displayed. "
            "Instead, the dispute engine indexes judicial load from National Judicial Data Grid APIs, "
            "highlighting systemic litigation backlogs, average disposal times, and tenancy dispute clusters to inform "
            "land value adjustments and risk assessments."
        ),
    },
    {
        "id": 5,
        "title": "Grounded Legal AI Assistant & Policy Simulation",
        "lower_third": "GROUNDED STATUTORY AI & SIMULATION SANDBOX | Gujarat Land Revenue Code § 65",
        "script": (
            "To bridge the gap between spatial data and complex land law, Bhumi-Niti introduces a grounded legal AI assistant. "
            "When asked about converting agricultural parcels for logistics use, our in-memory RAG pipeline analyzes the specific "
            "territorial jurisdiction. Because it is grounded directly in enacted statutes—including Section 65 of the Gujarat Land Revenue Code "
            "and tribal land protections under Section 73AA—it generates hallucination-free legal opinions with statutory citations. "
            "Complementing this, the Policy Simulation sandbox allows planners to test zoning scenarios, automatically projecting "
            "environmental clearances, infrastructure buffers, and statutory feasibility scores."
        ),
    },
    {
        "id": 6,
        "title": "State Knowledge Repository & Innovation Hub",
        "lower_third": "INDIA CODE REPOSITORY & MYGOV INNOVATION HUB | Req 15 & 16 Multi-Module",
        "script": (
            "Bhumi-Niti extends beyond GIS into a comprehensive institutional ecosystem. "
            "The Policy Repository integrates directly with India Code and state gazette feeds. "
            "Researchers can filter by revenue codes or town planning acts, access official PDFs, "
            "and run in-memory statutory synthesis on demand. "
            "Simultaneously, the Innovation Hub fulfills the ministry's mandate to crowdsource solutions under Problem Statement 26019. "
            "It hosts open hackathons for drone cadastral alignment, provides a formal grant application pipeline for academic fellowships, "
            "and tracks real-world pilot deployments from Dholera to Gautam Buddha Nagar."
        ),
    },
    {
        "id": 7,
        "title": "Impact, National Scalability & Closing",
        "lower_third": "NATIONAL DIGITAL PLATFORM FOR EVIDENCE-BASED LAND GOVERNANCE | MoRD",
        "script": (
            "With an architecture built entirely on open-source, vendor-neutral technologies—MapLibre GL JS, "
            "FastAPI, and Sentinel-2 satellite telemetry—Bhumi-Niti is engineered for rapid nationwide adoption. "
            "By unifying spatial precision, ethical dispute analytics, grounded statutory intelligence, "
            "and collaborative academic innovation, we provide administrators with the tools to transition "
            "from reactive dispute settlement to predictive, evidence-based governance. "
            "This is Bhumi-Niti: Empowering transparent, data-driven land administration for Viksit Bharat 2047. Thank you."
        ),
    },
]

# ------------------------------------------------------------------------------
# 2. HELPER UTILITIES & PRE-FLIGHT
# ------------------------------------------------------------------------------
def verify_server():
    """Verify that the FastAPI backend server is alive on http://localhost:8000."""
    try:
        req = urllib.request.Request(BASE_URL, headers={"User-Agent": "BhumiNitiAutomation/1.0"})
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                log_success(f"Verified local server is active at {BASE_URL}")
                return True
    except Exception as e:
        log_error(f"Cannot connect to {BASE_URL}: {e}")
        print(f"\n{C_YELLOW}Please start the Bhumi-Niti server in a separate terminal:{C_RESET}")
        print(f"  {C_BOLD}python run.py{C_RESET} or {C_BOLD}python main.py{C_RESET}\n")
        return False
    return False

def get_ffmpeg_path():
    """Find FFmpeg binary (from imageio_ffmpeg or system PATH)."""
    try:
        import imageio_ffmpeg
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        if os.path.exists(ffmpeg_exe):
            return ffmpeg_exe
    except Exception:
        pass
    return "ffmpeg"

def get_audio_duration(file_path: str, ffmpeg_bin: str) -> float:
    """Accurately extract duration of an audio file using FFmpeg."""
    cmd = [
        ffmpeg_bin,
        "-i", file_path,
        "-f", "null",
        "-"
    ]
    proc = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True, errors="ignore")
    # Parse Duration: 00:00:24.50
    for line in proc.stderr.splitlines():
        if "Duration:" in line:
            parts = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = parts.split(":")
            return float(h) * 3600 + float(m) * 60 + float(s)
    return 25.0

# ------------------------------------------------------------------------------
# 3. VOICE GENERATION MODULE (Edge-TTS)
# ------------------------------------------------------------------------------
async def generate_voiceovers():
    """Synthesize voiceover MP3 tracks for each scene using edge-tts."""
    import edge_tts

    log_step("[1/4]", "Generating Neural Voiceovers (Edge-TTS: en-IN-PrabhatNeural)...")
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    ffmpeg_bin = get_ffmpeg_path()
    durations = {}

    for scene in SCENES:
        sid = scene["id"]
        out_mp3 = TEMP_DIR / f"scene_{sid:02d}.mp3"
        
        # Check if already synthesized to avoid unnecessary re-generation
        if out_mp3.exists() and out_mp3.stat().st_size > 1000:
            dur = get_audio_duration(str(out_mp3), ffmpeg_bin)
            scene_dur = round(dur + 1.2, 2)
            durations[sid] = scene_dur
            log_success(f"Scene {sid} Voiceover cached -> {out_mp3.name} ({dur:.2f}s audio + 1.2s padding = {scene_dur:.2f}s total)")
            continue

        log_info(f"Synthesizing Scene {sid}: {scene['title']}...")
        # Edge-TTS synthesize
        communicate = edge_tts.Communicate(scene["script"], VOICE_NAME, rate="+0%", volume="+0%")
        await communicate.save(str(out_mp3))
        
        dur = get_audio_duration(str(out_mp3), ffmpeg_bin)
        # Add 1.2s padding for natural transition breathing room
        scene_dur = round(dur + 1.2, 2)
        durations[sid] = scene_dur
        log_success(f"Scene {sid} Voiceover saved -> {out_mp3.name} ({dur:.2f}s audio + 1.2s padding = {scene_dur:.2f}s total)")

    return durations

# ------------------------------------------------------------------------------
# 4. PLAYWRIGHT UI CHOREOGRAPHY MODULE
# ------------------------------------------------------------------------------
async def record_scene_choreography(durations: dict):
    """Programmatically drives Chromium via Playwright and records scene clips."""
    from playwright.async_api import async_playwright

    log_step("[2/4]", "Recording UI Choreography (Playwright Chromium 1080p)...")
    raw_video_dir = TEMP_DIR / "raw_recordings"
    raw_video_dir.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--hide-scrollbars",
            ]
        )
        
        scene_clips = {}

        for scene in SCENES:
            sid = scene["id"]
            target_duration = durations[sid]
            scene_dir = raw_video_dir / f"scene_{sid:02d}"
            scene_dir.mkdir(parents=True, exist_ok=True)

            log_info(f"Choreographing Scene {sid} ({target_duration:.2f}s target)...")
            start_scene_time = time.time()

            context = await browser.new_context(
                viewport={"width": WIDTH, "height": HEIGHT},
                record_video_dir=str(scene_dir),
                record_video_size={"width": WIDTH, "height": HEIGHT},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) BhumiNitiAutomation/1.0"
            )
            page = await context.new_page()

            # Execute scene-specific choreographed actions
            if sid == 1:
                # Scene 1: Landing, Masthead, GIGW Utility Bar, scroll
                await page.goto(f"{BASE_URL}/", wait_until="networkidle")
                await page.wait_for_timeout(2000)
                # Scroll slightly down to show GIS & Dossier integration
                await page.mouse.wheel(0, 150)
                await page.wait_for_timeout(3000)
                # Hover over role selector
                try:
                    await page.hover("#roleSelector", timeout=3000)
                except Exception:
                    pass
                await page.wait_for_timeout(2000)

            elif sid == 2:
                # Scene 2: Search "Sanand", click suggestion, wait for flyTo & spotlight
                await page.goto(f"{BASE_URL}/", wait_until="networkidle")
                await page.wait_for_timeout(1500)
                # Focus search input and type with human-like delay
                search_input = page.locator("#searchInput")
                await search_input.click()
                await search_input.press_sequentially("Sanand", delay=120)
                await page.wait_for_timeout(1000)
                
                # Check for suggestion dropdown or click search button
                suggestion = page.locator("#searchSuggestions .suggestion-item").first
                if await suggestion.count() > 0:
                    await suggestion.click()
                else:
                    await page.click("#searchBtn")
                
                # Wait for MapLibre flyTo and boundary spotlight to settle
                await page.wait_for_timeout(5000)
                # Hover over boundary checkbox
                try:
                    await page.hover("#checkSpotlight", timeout=2000)
                except Exception:
                    pass
                await page.wait_for_timeout(2000)

            elif sid == 3:
                # Scene 3: Satellite toggle, LULC Opacity slider, Legend hover
                await page.goto(f"{BASE_URL}/", wait_until="networkidle")
                # Search Sanand to establish context
                await page.fill("#searchInput", "Sanand")
                await page.click("#searchBtn")
                await page.wait_for_timeout(3500)
                
                # Switch to Satellite Base Map
                sat_btn = page.locator("#layerSat")
                if await sat_btn.count() > 0:
                    await sat_btn.click()
                await page.wait_for_timeout(2500)

                # Move LULC Opacity Slider back and forth
                opacity_slider = page.locator("#rngLulcOpacity")
                if await opacity_slider.count() > 0:
                    await page.evaluate("""() => {
                        const el = document.getElementById('rngLulcOpacity');
                        if (el) {
                            el.value = '0.90';
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    }""")
                    await page.wait_for_timeout(1500)
                    await page.evaluate("""() => {
                        const el = document.getElementById('rngLulcOpacity');
                        if (el) {
                            el.value = '0.45';
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    }""")
                    await page.wait_for_timeout(1500)
                    await page.evaluate("""() => {
                        const el = document.getElementById('rngLulcOpacity');
                        if (el) {
                            el.value = '0.70';
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    }""")
                
                # Hover over legend
                try:
                    await page.hover(".map-legend-box", timeout=2500)
                except Exception:
                    pass
                await page.wait_for_timeout(2000)

            elif sid == 4:
                # Scene 4: Right dossier, Accordion 2 & Accordion 3, Badges
                await page.goto(f"{BASE_URL}/", wait_until="networkidle")
                await page.fill("#searchInput", "Sanand")
                await page.click("#searchBtn")
                await page.wait_for_timeout(3000)
                
                # Expand Accordion 2 (Statutory Legal Framework)
                acc2 = page.locator("#acc2 .acc-header")
                if await acc2.count() > 0:
                    await acc2.click()
                await page.wait_for_timeout(2500)

                # Expand Accordion 3 (Dispute & Litigation Telemetry)
                acc3 = page.locator("#acc3 .acc-header")
                if await acc3.count() > 0:
                    await acc3.click()
                await page.wait_for_timeout(3000)

                # Hover over dispute metrics card
                try:
                    await page.hover("#acc3 .badge-red", timeout=2000)
                except Exception:
                    pass
                await page.wait_for_timeout(2000)

            elif sid == 5:
                # Scene 5: Grounded Legal AI Assistant & Policy Simulation
                await page.goto(f"{BASE_URL}/", wait_until="networkidle")
                # Search Sanand to populate dossier and expose active drawers
                await page.fill("#searchInput", "Sanand")
                await page.click("#searchBtn")
                await page.wait_for_timeout(3500)
                
                # Scroll down to AI & Simulation section
                await page.evaluate("""() => {
                    const el = document.getElementById('aiDrawer');
                    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }""")
                await page.wait_for_timeout(1500)

                # Type question in AI chat input
                ai_input = page.locator("#aiQuestionInput")
                if await ai_input.count() > 0:
                    await ai_input.click()
                    await ai_input.press_sequentially(
                        "Can agricultural land be converted to an industrial logistics park under Section 65?",
                        delay=45
                    )
                    await page.wait_for_timeout(1000)
                    # Submit query
                    send_btn = page.locator("#btnAskAI, .btn-ask-ai")
                    if await send_btn.count() > 0 and await send_btn.is_visible():
                        await send_btn.click()
                    else:
                        await ai_input.press("Enter")
                
                await page.wait_for_timeout(4500)

                # Toggle Policy Simulation Drawer
                await page.evaluate("""() => {
                    if (typeof toggleModule === 'function') {
                        toggleModule('simDrawer');
                    }
                    const simEl = document.getElementById('simDrawer');
                    if (simEl) simEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }""")
                await page.wait_for_timeout(2000)

                # Move buffer slider
                buf_slider = page.locator("#rngBuffer")
                if await buf_slider.count() > 0:
                    await page.evaluate("""() => {
                        const el = document.getElementById('rngBuffer');
                        if (el) {
                            el.value = '1200';
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                        }
                    }""")

            elif sid == 6:
                # Scene 6: Navigate to /knowledge-base, filter acts, navigate to /innovation
                await page.goto(f"{BASE_URL}/knowledge-base", wait_until="networkidle")
                await page.wait_for_timeout(3000)
                
                # Type filter in KB search
                kb_search = page.locator("#kbSearchInput")
                if await kb_search.count() > 0:
                    await kb_search.fill("Revenue")
                await page.wait_for_timeout(3000)

                # Navigate to /innovation
                await page.goto(f"{BASE_URL}/innovation", wait_until="networkidle")
                await page.wait_for_timeout(3000)
                # Click through tabs
                tab_academic = page.locator("button:has-text('Academic'), a:has-text('Academic')").first
                if await tab_academic.count() > 0:
                    await tab_academic.click()
                    await page.wait_for_timeout(2000)

            elif sid == 7:
                # Scene 7: Full Gujarat/National view, GIGW Footer, Closing
                await page.goto(f"{BASE_URL}/", wait_until="networkidle")
                await page.wait_for_timeout(2500)
                # Scroll down to showcase GIGW 3.0 Audit Footer
                await page.mouse.wheel(0, 600)
                await page.wait_for_timeout(4000)
                # Highlight footer compliance badge
                try:
                    await page.hover(".gov-footer-badge, .audit-badge", timeout=2000)
                except Exception:
                    pass
                await page.wait_for_timeout(3000)

            # Pad remaining time to precisely hit the target audio duration
            elapsed = time.time() - start_scene_time
            remaining_time = target_duration - elapsed
            if remaining_time > 0:
                await page.wait_for_timeout(int(remaining_time * 1000))

            # Close context to finalize WebM video file
            video_file = await page.video.path()
            await context.close()

            scene_clips[sid] = video_file
            log_success(f"Scene {sid} Captured ({time.time() - start_scene_time:.2f}s) -> {Path(video_file).name}")

        await browser.close()
        return scene_clips

# ------------------------------------------------------------------------------
# 5. MULTIMEDIA COMPOSITION ENGINE (FFmpeg)
# ------------------------------------------------------------------------------
def build_final_video(durations: dict, scene_clips: dict):
    """Combines voiceovers, video clips, ambient background audio, and lower-thirds."""
    log_step("[3/4]", "Rendering & Audio Synchronization (FFmpeg 1080p 60FPS)...")
    ffmpeg_bin = get_ffmpeg_path()
    processed_scenes = []

    # Process each individual scene: sync video speed/duration to audio and add lower-third card
    for scene in SCENES:
        sid = scene["id"]
        raw_video = scene_clips[sid]
        audio_file = TEMP_DIR / f"scene_{sid:02d}.mp3"
        scene_dur = durations[sid]
        out_scene_mp4 = TEMP_DIR / f"synced_scene_{sid:02d}.mp4"
        if out_scene_mp4.exists() and out_scene_mp4.stat().st_size > 10000:
            log_success(f"Scene {sid} already synced (cached) -> {out_scene_mp4.name}")
            processed_scenes.append(out_scene_mp4)
            continue

        log_info(f"Synchronizing Scene {sid} to {scene_dur:.2f}s...")

        # Subtitle / Lower-Third Text escaping
        sub_text = scene["lower_third"].replace(":", "\\:").replace("'", "\\'").replace("|", "\\|")
        title_text = f"SCENE {sid}: {scene['title'].upper()}".replace(":", "\\:").replace("'", "\\'")

        # FFmpeg filtergraph for scene:
        # 1. Scale/Pad to 1920x1080 at 60fps
        # 2. Draw lower-third background bar and text
        # 3. Trim to exact scene duration
        filter_graph = (
            f"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
            f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=60,"
            f"drawbox=y=ih-110:color=#082136@0.85:width=iw:height=90:t=fill,"
            f"drawbox=y=ih-110:color=#EA580C@1.0:width=iw:height=4:t=fill,"
            f"drawtext=text='{title_text}':fontcolor=white:fontsize=22:font='Segoe UI':x=60:y=h-95,"
            f"drawtext=text='{sub_text}':fontcolor=#94A3B8:fontsize=16:font='Segoe UI':x=60:y=h-62,"
            f"tpad=stop_mode=clone:stop_duration=5[v]"
        )

        cmd = [
            ffmpeg_bin,
            "-y",
            "-i", raw_video,
            "-i", str(audio_file),
            "-filter_complex", filter_graph,
            "-map", "[v]",
            "-map", "1:a",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "18",
            "-c:a", "aac",
            "-b:a", "192k",
            "-t", str(scene_dur),
            str(out_scene_mp4)
        ]

        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="ignore")
        if res.returncode != 0:
            log_warn(f"Drawtext filter warning on Scene {sid}. Fallback without text overlay...")
            # Fallback simple sync without drawtext (in case font is missing)
            cmd_fallback = [
                ffmpeg_bin,
                "-y",
                "-i", raw_video,
                "-i", str(audio_file),
                "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=60",
                "-c:v", "libx264",
                "-preset", "fast",
                "-crf", "18",
                "-c:a", "aac",
                "-b:a", "192k",
                "-t", str(scene_dur),
                str(out_scene_mp4)
            ]
            subprocess.run(cmd_fallback, check=True)

        processed_scenes.append(out_scene_mp4)
        log_success(f"Scene {sid} synchronized -> {out_scene_mp4.name}")

    # Generate synthetic ambient documentary score (sine chord bed) at -24dB
    total_duration = sum(durations.values())
    ambient_audio = (TEMP_DIR / "ambient_bed.aac").resolve()
    if not ambient_audio.exists() or ambient_audio.stat().st_size == 0:
        log_info(f"Synthesizing ambient documentary audio bed ({total_duration:.2f}s @ -24dB)...")
        ambient_cmd = [
            ffmpeg_bin,
            "-y",
            "-f", "lavfi",
            "-i", f"aevalsrc=0.012*sin(2*PI*110*t)+0.008*sin(2*PI*164.81*t)+0.006*sin(2*PI*220*t):s=48000:d={total_duration + 5}",
            "-af", f"volume=0.08,lowpass=f=800,afade=t=in:st=0:d=3,afade=t=out:st={total_duration-2}:d=2",
            "-c:a", "aac",
            "-b:a", "128k",
            str(ambient_audio)
        ]
        subprocess.run(ambient_cmd, check=True)

    # Concatenate all 7 scenes using FFmpeg concat demuxer
    concat_list = (TEMP_DIR / "concat_list.txt").resolve()
    with open(concat_list, "w", encoding="utf-8") as f:
        for p_scene in processed_scenes:
            p_str = p_scene.resolve().as_posix()
            f.write(f"file '{p_str}'\n")

    log_info("Merging all 7 scenes and mixing ambient audio track...")
    final_output = Path(OUTPUT_VIDEO).resolve()

    final_cmd = [
        ffmpeg_bin,
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list),
        "-i", str(ambient_audio),
        "-filter_complex", "[0:a][1:a]amix=inputs=2:duration=first:weights=1.0 0.15[aout]",
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "256k",
        "-movflags", "+faststart",
        str(final_output)
    ]

    subprocess.run(final_cmd, check=True)
    return final_output

# ------------------------------------------------------------------------------
# 6. MAIN PIPELINE EXECUTION
# ------------------------------------------------------------------------------
def print_banner():
    print(f"{C_BOLD}{C_CYAN}")
    print("=" * 80)
    print("   BHUMI-NITI (भूमि-नीति) : FLAGSHIP VIDEO PRODUCTION PIPELINE")
    print("   National Digital Platform for Evidence-Based Land Governance")
    print("   Problem Statement 26019 | Ministry of Rural Development (DoLR)")
    print("=" * 80)
    print(f"{C_RESET}")

def main():
    print_banner()

    # Step 0: Pre-flight checks
    if not verify_server():
        sys.exit(1)

    try:
        # Step 1: Voice Generation via Edge-TTS
        durations = asyncio.run(generate_voiceovers())

        # Step 2: Browser UI Choreography via Playwright
        scene_clips = asyncio.run(record_scene_choreography(durations))

        # Step 3: FFmpeg Synchronization and Rendering
        final_mp4 = build_final_video(durations, scene_clips)

        # Step 4: Done!
        file_size_mb = final_mp4.stat().st_size / (1024 * 1024)
        total_runtime = sum(durations.values())
        minutes = int(total_runtime // 60)
        seconds = int(total_runtime % 60)

        log_step("[4/4]", f"Walkthrough Complete: ./{OUTPUT_VIDEO}")
        print(f"\n{C_BOLD}{C_GREEN}================================================================================")
        print(f"  ✓ PRODUCTION SUCCESSFUL: {OUTPUT_VIDEO}")
        print(f"  • Resolution : 1920x1080 (1080p 60 FPS)")
        print(f"  • Codec      : H.264 / AAC Stereo")
        print(f"  • Total Time : {minutes}m {seconds:02d}s ({total_runtime:.1f}s)")
        print(f"  • File Size  : {file_size_mb:.2f} MB")
        print(f"  • Scenes     : 7 Scenes Synchronized with en-IN-PrabhatNeural")
        print("================================================================================")
        print(f"{C_RESET}")

    except Exception as e:
        log_error(f"Pipeline failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
