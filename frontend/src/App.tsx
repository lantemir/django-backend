import React from 'react';
import logo from './logo.svg';
import './App.css';
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import Home from './pages/Home';
import './css/bootstrap/bootstrap.min.css';


function App() {

  const router = createBrowserRouter([
    {
      path: "/",
      element: <Home/>,
    },
  ]);


  return (
    <RouterProvider router={router} />
  );
}

export default App;
