async function fetchBins() {
    const response = await fetch('/bins');
    const bins = await response.json();
    const binsList = document.getElementById('bins');
    binsList.innerHTML = bins.map(bin => `<li>Lixeira ${bin.bin_id} - Nível: ${bin.level}%</li>`).join('');
}

async function fetchOptimizedRoute() {
    const response = await fetch('/optimize-route');
    const { route, distance } = await response.json();
    document.getElementById('route').innerText = `Rota: ${route.join(' -> ')} (Distância: ${distance} km)`;
}

fetchBins();
fetchOptimizedRoute();
