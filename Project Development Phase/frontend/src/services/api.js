import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

// Request interceptor: attach JWT token from localStorage
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("token");
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

// Response interceptor: handle 401 globally
// Only redirect if we're NOT on the login or register page
api.interceptors.response.use(
    (response) => response,
    (error) => {
        if (error.response && error.response.status === 401) {
            const currentPath = window.location.pathname;
            const isAuthPage = currentPath === "/" || currentPath === "/register";

            if (!isAuthPage) {
                // Session expired — clear storage and redirect to login
                localStorage.removeItem("token");
                localStorage.removeItem("user");
                window.location.href = "/";
            }
        }
        return Promise.reject(error);
    }
);

export default api;