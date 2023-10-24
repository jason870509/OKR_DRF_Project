import axios from "axios";

function useAxios() {
  const instance = axios.create({
    timeout: 1000,
    // baseURL: "http://localhost:3000",
    headers: {
      "Content-Type": "application/json",
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
      return error;
    }
  );

  return instance;
}

export default useAxios;
