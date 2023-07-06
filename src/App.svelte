<script>
  import Login from "./pages/Login.svelte";
  import Main from "./pages/Main.svelte";
  import Signup from "./pages/Signup.svelte";
  import Write from "./pages/Write.svelte";
  import NotFount from "./pages/NotFount.svelte";
  import Router from "svelte-spa-router";
  import "./css/style.css";
  const routes = {
    "/": Main,
    "/login": Login,
    "/signup": Signup,
    "/write": Write,
    "*": NotFount,
  };
</script>

<Router {routes} />

<main />

<style>
  div {
    color: red;
  }
</style>
