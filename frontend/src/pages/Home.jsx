import React from "react";
import axios from "axios";
import * as bases from '../components/bases';
import { useAppDispatch } from "../app/hooks";


export const GET_ALL_MESSAGE_LOAD = "GET_ALL_MESSAGE_LOAD";
export const GET_ALL_MESSAGE_DATA = "GET_ALL_MESSAGE_DATA";
export const GET_ALL_MESSAGE_ERROR = "GET_ALL_MESSAGE_ERROR";
export const GET_ALL_MESSAGE_FAIL = "GET_ALL_MESSAGE_FAIL";
export const GET_ALL_MESSAGE_RESET = "GET_ALL_MESSAGE_RESET";

export function GetAllMessageReducer(state={}, action = null) {
    switch (action.type){
        case GET_ALL_MESSAGE_LOAD:
            return { load: true }
        case GET_ALL_MESSAGE_DATA:
            return { load: false, data: action.payload }
        case GET_ALL_MESSAGE_ERROR:
            return { error: 'Ошибка на сервере' }
        case GET_ALL_MESSAGE_FAIL:
            return { error: 'Ошибка на клиенте' }
        case GET_ALL_MESSAGE_RESET:
            return {}
        default:
            return state
    }
}


function Home() {
    const dispatch = useAppDispatch();

    async function GetAllSms() {
        dispatch({type: GET_ALL_MESSAGE_LOAD})

        const config = {
            method: "GET",
            timeout: 5000,
            url: `/api/chat/?page=1&limit=3`
        }
        const response = await axios(config)
        console.log(response.data)

        dispatch({type: GET_ALL_MESSAGE_DATA, payload: response.data})
     
    }

    

    return(
        <bases.Base1>
            <div>
                <div>Home</div>
                <button className="btn btn-lg btn-outline-danger" onClick={GetAllSms}>GetAllSms</button>
            </div>
        </bases.Base1>
    )
}

export default Home