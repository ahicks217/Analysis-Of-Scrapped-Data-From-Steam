document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("liveSearch");
    const table = document.getElementById("gamesTable");

    if (!searchInput || !table) return;

    const tbody = table.querySelector("tbody");
    const form = document.querySelector("form");

    // Create "no results" message if it does not already exist
    let noResults = document.getElementById("noResults");
    if (!noResults) {
        noResults = document.createElement("div");
        noResults.id = "noResults";
        noResults.textContent = "No matching games found.";
        noResults.style.display = "none";
        table.parentNode.insertBefore(noResults, table);
    }

    // Create button container
    const controls = document.createElement("div");
    controls.className = "table-controls";

    // Button to reload page and get latest rendered data
    const refreshBtn = document.createElement("button");
    refreshBtn.type = "button";
    refreshBtn.textContent = "Get Latest Info";
    refreshBtn.className = "action-btn";

    refreshBtn.addEventListener("click", function () {
        window.location.reload();
    });

    // Button to sort by newest/oldest inserted using ID
    const sortBtn = document.createElement("button");
    sortBtn.type = "button";
    sortBtn.textContent = "Show Newest Inserted";
    sortBtn.className = "action-btn";

    let newestFirst = true;

    sortBtn.addEventListener("click", function () {
        sortTableById(newestFirst);
        sortBtn.textContent = newestFirst
            ? "Show Oldest Inserted"
            : "Show Newest Inserted";
        newestFirst = !newestFirst;
    });

    controls.appendChild(refreshBtn);
    controls.appendChild(sortBtn);

    // Insert buttons below the search form
    if (form) {
        form.insertAdjacentElement("afterend", controls);
    } else {
        table.parentNode.insertBefore(controls, table);
    }

    function getRows() {
        return Array.from(tbody.querySelectorAll("tr"));
    }

    function filterTable() {
        const filter = searchInput.value.toLowerCase().trim();
        let visibleCount = 0;

        getRows().forEach(row => {
            const text = row.innerText.toLowerCase();
            const match = text.includes(filter);

            row.style.display = match ? "" : "none";

            if (match) {
                visibleCount++;
            }
        });

        noResults.style.display = visibleCount === 0 ? "block" : "none";
    }

    function sortTableById(desc = true) {
        const rows = getRows();

        rows.sort((a, b) => {
            const idA = parseInt(a.cells[0]?.textContent.trim(), 10) || 0;
            const idB = parseInt(b.cells[0]?.textContent.trim(), 10) || 0;
            return desc ? idB - idA : idA - idB;
        });

        rows.forEach(row => tbody.appendChild(row));

        // Keep search results active after sorting
        filterTable();
    }

    // Live search while typing
    searchInput.addEventListener("keyup", filterTable);

    // Auto-focus search box
    searchInput.focus();

    // Press "/" to focus search quickly
    document.addEventListener("keydown", function (e) {
        if (e.key === "/" && document.activeElement !== searchInput) {
            e.preventDefault();
            searchInput.focus();
        }
    });

    // Default display: newest inserted first
    sortTableById(true);
    filterTable();
});