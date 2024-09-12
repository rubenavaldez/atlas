import axios from "axios"
import { ACCESS_TOKEN } from "./constants"

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
})

// validate token useing built in axios
api.interceptors.request.use(
    (config)=>{
        const token: string|null = localStorage.getItem(ACCESS_TOKEN)
        if (token){
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error)=>{
        return Promise.reject(error)
    }
)

export default api