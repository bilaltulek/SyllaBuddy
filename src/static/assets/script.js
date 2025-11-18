document.addEventListener("DOMContentLoaded", () => {

    // ===== Temporary fake syllabus history =====
    let historyData = [
        {
            name: "CS 3345 Syllabus",
            course: "CS 3345 – Data Structures",
            date: "Jan 28, 2025",
            ics: "ics/cs3345.ics"
        },
        {
            name: "CS 3377 Syllabus",
            course: "CS 3377 – Systems Programming",
            date: "Jan 22, 2025",
            ics: "ics/cs3377.ics"
        },
        {
            name: "PHYS 2325 Syllabus",
            course: "Physics I",
            date: "Jan 15, 2025",
            ics: "ics/phys2325.ics"
        }
    ];

    const historyList = document.getElementById("historyList");

    function renderHistory() {
        historyList.innerHTML = "";

        historyData.forEach(item => {
            const div = document.createElement("div");
            div.className = "history-item";

            div.innerHTML = `
                <div class="history-left">
                    <span class="item-name">${item.name}</span>
                    <span class="item-course">${item.course}</span>
                    <span class="item-date">Uploaded: ${item.date}</span>
                </div>

                <div class="download-btn" onclick="downloadICS('${item.ics}')">
                    <img src="../static/assets/arrow.png" alt="download arrow">
                </div>
            `;

            historyList.appendChild(div);
        });
    }

    renderHistory();

    // ICS file download
    window.downloadICS = function (filePath) {
        console.log("Downloading:", filePath);
        window.location.href = filePath;
    };
});