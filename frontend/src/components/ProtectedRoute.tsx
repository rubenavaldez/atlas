/** @format */

import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import { useEffect, useState } from "react";
import api from "../api";
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants";

// check for access token before allowing user to access this route
export const ProtectedRoute: any ({children: any})=>{
    const [isAuthorized, setIsAuthorized] = useState<boolean|null>(null)

    useEffect(()=>{
        auth().catch(()=> setIsAuthorized(false))
    },[])

    const refreshToken: ()=>void = async() =>{
        const refreshToken = localStorage.getItem(REFRESH_TOKEN)
        try{
            const res = await api.post("/api/token/refresh/",{refresh: refreshToken})
            if (res.status ===200){
                localStorage.setItem(ACCESS_TOKEN, res.data.access)
                setIsAuthorized(true)
            }else{
                setIsAuthorized(false)
            }
        }
    }

    const auth: any = async () =>{
        const token: string | null = localStorage.getItem(ACCESS_TOKEN)
        if (!token) {
            setIsAuthorized(false)
            return
        }
        const decoded = jwtDecode(token)
        const now = Date.now() / 1000  // in seconds 
        const tokenExpiration: number  = decoded?.exp || now
        if (tokenExpiration < now){
            await refreshToken()
        }else {
            setIsAuthorized(true)
        }
    

    }

    if (isAuthorized === null){
        return <div>Loading...</div>
    }

    return isAuthorized ? children : <Navigate to='login'/> // auto reroute to login page
}