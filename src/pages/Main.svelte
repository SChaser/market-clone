<script>
  import { onMount } from "svelte";
  import Footer from "../components/Footer.svelte";
  import { getDatabase, ref, onValue } from "firebase/database";

  const calcTime = (timestamp) => {
    //한국시간 UTC+9을 세계시간으로 맞추기
    const curTime = new Date().getTime() - 9 * 60 * 60 * 1000;
    const time = new Date(curTime - timestamp);
    const hour = time.getHours();
    const minute = time.getMinutes();
    const second = time.getSeconds();

    if (hour > 0) return `${hour}시간 전`;
    else if (minute > 0) return `${minute}분 전`;
    else if (second > 0) return `${second}초 전`;
    else return "방금 전";
  };

  let hour = new Date().getHours();
  let min = new Date().getMinutes();

  $: items = [];

  const db = getDatabase();
  const itmesRef = ref(db, "items/");
  //onMount() 안에 넣으면 렌더링 될때마다 호출이 된다.
  onMount(() => {
    onValue(itmesRef, (snapshot) => {
      const data = snapshot.val();
      items = Object.values(data).reverse();
    });
  });
</script>

<header>
  <div class="info-bar">
    <div class="info-bar__time">{hour}:{min}</div>
    <div class="info-bar__icons">
      <img src="assets/chart-bar.svg" alt="chart-bar" />
      <img src="assets/wifi.svg" alt="wifi" />
      <img src="assets/battery.svg" alt="battery" />
    </div>
  </div>
  <div class="menu-bar">
    <div class="menu-bar__location">
      <div class="menu-bar__locationame">역삼1동</div>
      <div class="menu-bar__location-icon">
        <img src="assets/arrow-down.svg" alt="" />
      </div>
    </div>
    <div class="menu-bar__icons2">
      <img src="assets/search.svg" alt="search" />
      <img src="assets/menu.svg" alt="menu" />
      <img src="assets/alert.svg" alt="alert" />
    </div>
  </div>
</header>
<div class="item-list__info-title" />
<div class="item-list__info-meta" />
<div />

<main>
  {#each items as item}
    <div class="item-list">
      <div class="item-list__img">
        <img alt={item.title} src={item.imgUrl} />
      </div>
      <div class="item-list__info">
        <div class="item-list__info-title">{item.title}</div>
        <div class="item-list__info-meta">
          {item.place}
          {calcTime(item.insertAt)}
        </div>
        <div class="item-list__info-price">{item.price}</div>
        <div class="item-list__info-description">{item.description}</div>
      </div>
    </div>
  {/each}

  <a class="write-btn" href="#/write">+ 글쓰기</a>
</main>
<Footer location="home" />
<div class="media-info-msg">화면 사이즈를 줄여주세요</div>

<style>
  .info-bar__time {
    color: blue;
  }
</style>
