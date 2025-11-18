document.addEventListener("DOMContentLoaded", function () {

    // --- Set Current Month Title ---
    const monthTitle = document.getElementById("currentMonth");

    const today = new Date();
    const monthName = today.toLocaleString("default", { month: "long" });
    const year = today.getFullYear();

    monthTitle.textContent = `${monthName} ${year}`;
});

document.addEventListener("DOMContentLoaded", () => {
    
    // ===========================
    // 1. Fake event data for now
    // ===========================
    let events = [
        {
            day: "12",
            name: "Exam 1",
            syllabus: "CS 3345 – Data Structures",
            ics: "files/exam1.ics"
        },
        {
            day: "18",
            name: "Project Deadline",
            syllabus: "CS 3377 – Systems Programming",
            ics: "files/project.ics"
        },
        {
            day: "21",
            name: "Quiz 5",
            syllabus: "CS 1337 – Intro to CS",
            ics: "files/quiz5.ics"
        },
        {
            day: "28",
            name: "Lab Due",
            syllabus: "CS 1200 – Intro to CE",
            ics: "files/lab.ics"
        }
    ];

    // ===========================
    // 2. Render events into page
    // ===========================
    const eventList = document.getElementById("eventList");

    function renderEvents() {
        eventList.innerHTML = "";

        events.forEach(evt => {
            const div = document.createElement("div");
            div.className = "event-item";

            div.innerHTML = `
                <div class="event-left">
                    <div class="event-date">${evt.day}</div>

                    <div class="event-details">
                        <span class="event-name">${evt.name}</span>
                        <span class="event-syllabus">${evt.syllabus}</span>
                    </div>
                </div>

                <div class="event-right">
                    <div class="manage-text">Export Event</div>
                    <div class="download-btn" onclick="downloadICS('${evt.ics}')">
                        <img src="arrow.png" alt="download">
                    </div>
                </div>
            `;

            eventList.appendChild(div);
        });
    }

    renderEvents();

    // ===========================
    // 3. ICS download handler
    // ===========================
    window.downloadICS = function (filePath) {
        console.log("Downloading:", filePath);
        window.location.href = filePath;
    };


    // ===========================
    // 4. Pagination (fake for now)
    // ===========================
    const pagination = document.getElementById("pagination");

    function renderPagination() {
        pagination.innerHTML = `
            <span class="page active">1</span>
            <span class="page">2</span>
            <span class="page">3</span>
            <span class="page dots">...</span>
            <span class="page">8</span>
        `;
    }

    renderPagination();
});
