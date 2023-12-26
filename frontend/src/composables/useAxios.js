import axios from "axios";

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");

    for (const item of cookies) {
      const cookie = item.trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }

  return cookieValue;
}

function useAxios() {
  const instance = axios.create({
    // timeout: 1000,
    // baseURL: "http://localhost:3000",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
      //   Authorization: "Bearer SOMEJWTTOKEN",
    },
  });

  instance.interceptors.request.use((config) => {
    // console.log(config);
    return config;
  });

  instance.interceptors.response.use(
    (response) => {
      // console.log(response);
      return response;
    },
    (error) => {
      console.log(error);
      throw error;
    }
  );

  return instance;
}

export default useAxios;
