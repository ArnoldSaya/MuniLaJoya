import axios from 'axios'

const apiBaseURL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:5000/api'

export const apiClient = axios.create({
  baseURL: apiBaseURL,
  timeout: 10000,
})