let lastTime = 0;

setInterval(() => {
    fetch("http://127.0.0.1:8000/smart-progress/1")
    .then(res => res.json())
    .then(data => {
        console.log("🎯 PROGRESS:", data);

        createProgressBar(data.ilerleme_yuzde);
        createInfoBox(data);
    });

    const video = document.querySelector("video");
    if (!video) return;
    if (video.paused) return;

    const urlParams = new URLSearchParams(window.location.search);
    const videoId = urlParams.get("v");
    if (!videoId) return;

    const currentTime = Math.floor(video.currentTime);
    const duration = Math.floor(video.duration);

    if (currentTime === lastTime) return;
    lastTime = currentTime;

    console.log("🚀KEREMOS🚀", {
        video_id: videoId,
        current_time: currentTime,
        duration: duration
    });

    fetch("http://127.0.0.1:8000/watch/progress", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            youtube_video_id: videoId,
            current_time: currentTime,
            duration: duration
        })
    })
    .then(res => res.json())
    .then(data => console.log("✅ API:", data))
    .catch(err => console.error("❌ ERROR:", err));

}, 5000);

function createProgressBar(percent) {
    let bar = document.getElementById("keremos-bar");

    if (!bar) {
        bar = document.createElement("div");
        bar.id = "keremos-bar";
        bar.style.position = "fixed";
        bar.style.top = "0";
        bar.style.left = "0";
        bar.style.height = "6px";
        bar.style.background = "red";
        bar.style.zIndex = "9999";
        document.body.appendChild(bar);
    }

    bar.style.width = percent + "%";
}

function createInfoBox(data) {
    let box = document.getElementById("keremos-box");

    if (!box) {
        box = document.createElement("div");
        box.id = "keremos-box";
        box.style.position = "fixed";
        box.style.top = "10px";
        box.style.right = "10px";
        box.style.background = "black";
        box.style.color = "white";
        box.style.padding = "10px";
        box.style.zIndex = "9999";
        box.style.fontSize = "14px";
        document.body.appendChild(box);
    }

    box.innerHTML = `
        🎯 ${data.ilerleme_yuzde}% tamamlandı <br>
        ⏱ Kalan: ${data.kalan_saat} saat <br>
        🔥 6 saat/gün → ${data.gunde_6_saat_ile_kac_gun} gün <br>
        ⚡ Bu hızla → ${data.bu_hizla_kac_gun} gün
    `;
}