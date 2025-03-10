import { configureStore, ThunkAction, Action, getDefaultMiddleware } from '@reduxjs/toolkit';
// import counterReducer from '../features/counter/counterSlice';
import { combineReducers } from 'redux';
import thunk from "redux-thunk"

import { GetAllMessageReducer } from '../pages/Home';

const globalReducer = combineReducers({
  GetAllMessage: GetAllMessageReducer
})

const initialState = {

}

export const store = configureStore({
  reducer: globalReducer,
  devTools: true,
  middleware: (getDefaultMiddleware) =>getDefaultMiddleware().concat(thunk),
  preloadedState: initialState,
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
