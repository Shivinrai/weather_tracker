document.addEventListener('DOMContentLoaded', function() {
    const locationInput = document.getElementById('locationInput');
    const searchBtn = document.getElementById('searchBtn');
    const loading = document.getElementById('loading');
    const weatherResult = document.getElementById('weatherResult');
    const errorMessage = document.getElementById('errorMessage');
    
    const tempElement = document.getElementById('temp');
    const locationElement = document.getElementById('location');
    const descriptionElement = document.getElementById('description');
    const feelsLikeElement = document.getElementById('feelsLike');
    const humidityElement = document.getElementById('humidity');
    const windSpeedElement = document.getElementById('windSpeed');

    function showLoading() {
        loading.classList.remove('hidden');
        weatherResult.classList.add('hidden');
        errorMessage.classList.add('hidden');
    }

    function hideLoading() {
        loading.classList.add('hidden');
    }

    function showError(message) {
        hideLoading();
        errorMessage.querySelector('p').textContent = message;
        errorMessage.classList.remove('hidden');
        weatherResult.classList.add('hidden');
    }

    function showWeather(data) {
        hideLoading();
        
        tempElement.textContent = Math.round(data.temperature);
        locationElement.textContent = `${data.location}, ${data.country}`;
        descriptionElement.textContent = data.description;
        feelsLikeElement.textContent = `${Math.round(data.feels_like)}°C`;
        humidityElement.textContent = `${data.humidity}%`;
        windSpeedElement.textContent = `${data.wind_speed} m/s`;
        
        weatherResult.classList.remove('hidden');
        errorMessage.classList.add('hidden');
    }

    async function fetchWeather(location) {
        try {
            showLoading();
            
            const response = await fetch('/api/weather', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ location: location })
            });
            
            const data = await response.json();
            
            if (data.error) {
                showError(data.error);
            } else {
                showWeather(data);
            }
        } catch (error) {
            showError('Failed to fetch weather data. Please try again.');
            console.error('Error:', error);
        }
    }

    function handleSearch() {
        const location = locationInput.value.trim();
        
        if (!location) {
            showError('Please enter a location');
            return;
        }
        
        fetchWeather(location);
    }

    searchBtn.addEventListener('click', handleSearch);
    
    locationInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            handleSearch();
        }
    });

    locationInput.addEventListener('input', function() {
        if (errorMessage.classList.contains('hidden') === false) {
            errorMessage.classList.add('hidden');
        }
    });

    locationInput.focus();
});