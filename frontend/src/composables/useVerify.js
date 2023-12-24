import useAxios from "./useAxios";
import { useUserStore } from "../stores/user";

export function useVerify() {
  const verifyAPI = async () => {
    const axios = useAxios();
    const userStore = useUserStore();
    const token = {
      token: localStorage.getItem("access"),
    };

    if (userStore.login) {
      try {
        await axios.post("/api/api/token/verify/", token);
        userStore.login = true;
        console.log("userStore.login", userStore.login);
      } catch (err) {
        userStore.login = false;
        console.log("userStore.login", userStore.login);
      }
    }
  };

  return { verifyAPI };
}
