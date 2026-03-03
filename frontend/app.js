// Core Javascript for Frontend using Vanilla JS

const API_BASE = '/api';

// Simple Router
function showSection(sectionId) {
    document.querySelectorAll('main > div').forEach(el => el.classList.add('hidden'));
    document.getElementById(`section-${sectionId}`).classList.remove('hidden');

    if (sectionId === 'dashboard') loadDashboardData();
    if (sectionId === 'scans') loadScanJobs();
}

// Data Loaders
async function fetchAPI(endpoint, method = 'GET', body = null) {
    const opts = { method, headers: { 'Content-Type': 'application/json' } };
    if (body) opts.body = JSON.stringify(body);

    try {
        const res = await fetch(`${API_BASE}${endpoint}`, opts);
        return await res.json();
    } catch (err) {
        console.error('API Error:', err);
        return null;
    }
}

async function loadDashboardData() {
    const stats = await fetchAPI('/stats');
    if (stats) {
        document.getElementById('stat-assets').innerText = stats.total_assets;
        document.getElementById('stat-services').innerText = stats.total_services;
        document.getElementById('stat-scans').innerText = stats.total_scans;
    }

    const assets = await fetchAPI('/assets?limit=10');
    const tbody = document.getElementById('assets-table-body');
    if (assets && assets.length > 0) {
        tbody.innerHTML = assets.map(a => `
            <tr class="hover:bg-gray-800/50 transition-colors">
                <td class="px-6 py-4 font-mono text-blue-400">${a.ip}</td>
                <td class="px-6 py-4">${a.hostname || '-'}</td>
                <td class="px-6 py-4 text-xs">${new Date(a.first_seen).toLocaleString()}</td>
                <td class="px-6 py-4"><span class="bg-gray-700/50 text-gray-300 px-2 py-1 rounded-md text-xs border border-gray-600">${a.tags || 'untagged'}</span></td>
            </tr>
        `).join('');
    } else {
        tbody.innerHTML = `<tr><td colspan="4" class="px-6 py-8 text-center text-gray-500">No assets discovered yet.</td></tr>`;
    }
}

async function loadScanJobs() {
    const jobs = await fetchAPI('/scans');
    const list = document.getElementById('scan-jobs-list');
    if (jobs && jobs.length > 0) {
        list.innerHTML = jobs.map(j => {
            const color = j.status === 'completed' ? 'text-green-400' : (j.status === 'failed' ? 'text-red-400' : 'text-yellow-400');
            return `
            <li class="bg-gray-800/50 rounded-lg p-4 border border-gray-700 flex justify-between items-center">
                <div>
                    <span class="font-mono text-white text-sm block mb-1">${j.target}</span>
                    <span class="text-xs text-gray-500">${new Date(j.started_at).toLocaleString()}</span>
                </div>
                <div class="flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-current ${color}"></span>
                    <span class="text-sm font-medium ${color} capitalize">${j.status}</span>
                </div>
            </li>
        `}).join('');
    }
}

async function submitScan() {
    const target = document.getElementById('scan-target').value;
    if (!target) return;

    // In a real app we parse DSL or send POST properly.
    // Ensure we trigger it correctly
    const res = await fetch(`${API_BASE}/scans?target=${encodeURIComponent(target)}`, { method: 'POST' });
    if (res.ok) {
        loadScanJobs();
        document.getElementById('scan-target').value = '';
        setTimeout(loadDashboardData, 2000); // refresh dash
    }
}

async function performSearch() {
    const query = document.getElementById('search-input').value;
    const resultsGrid = document.getElementById('search-results-grid');
    resultsGrid.innerHTML = `<div class="col-span-full text-center py-10 text-gray-500">Searching...</div>`;

    const results = await fetchAPI(`/search?query=${encodeURIComponent(query)}`);
    if (results && results.length > 0) {
        resultsGrid.innerHTML = results.map(r => `
            <div class="glass-panel rounded-xl overflow-hidden hover:border-blue-500/50 transition-colors">
                <div class="bg-gray-800/80 px-4 py-3 border-b border-gray-700 flex justify-between items-center">
                    <span class="font-mono text-blue-400 font-bold">${r.protocol.toUpperCase()} / ${r.port}</span>
                    <span class="text-xs text-gray-400">ID: ${r.id}</span>
                </div>
                <div class="p-4">
                    <p class="text-gray-300 text-sm mb-2"><span class="text-gray-500">Product:</span> ${r.product || 'Unknown'} ${r.version || ''}</p>
                    ${r.banner ? `<div class="bg-black/50 p-2 rounded border border-gray-800 mt-2"><code class="text-xs text-emerald-400 font-mono line-clamp-3">${r.banner}</code></div>` : ''}
                </div>
            </div>
        `).join('');
    } else {
        resultsGrid.innerHTML = `<div class="col-span-full text-center py-10 text-gray-500">No services found matching the query.</div>`;
    }
}

// Initial load
window.onload = () => {
    loadDashboardData();
    setInterval(loadDashboardData, 10000); // auto-refresh stats
};
