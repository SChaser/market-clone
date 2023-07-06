<script>
  import { getDatabase, ref, set, push } from "firebase/database";
  import Footer from "../components/Footer.svelte";
  import {
    getStorage,
    getDownloadURL,
    ref as refImage,
    uploadBytes,
  } from "firebase/storage";

  let title;
  let price;
  let description;
  let place;
  let files;

  const storage = getStorage();
  const db = getDatabase();

  // 'file' comes from the Blob or File API
  // uploadBytes(storageRef, files).then((snapshot) => {
  //   console.log("Uploaded a blob or file!");
  // });

  //글쓰기
  function writeUserData(imgUrl) {
    push(ref(db, "items/"), {
      title,
      price,
      description,
      place,
      insertAt: new Date().getTime(),
      imgUrl,
    });
    alert("글쓰기 완료");
    window.location.hash = "/";
  }

  //이미지 업로드
  const uploadFile = async () => {
    const file = files[0];
    const name = file.name;
    const imgRef = refImage(storage, name);
    await uploadBytes(imgRef, file);
    const url = await getDownloadURL(imgRef);
    return url;
  };

  //이미지 조회
  const handleSubmit = async () => {
    const url = await uploadFile();
    writeUserData(url);
  };
</script>

<form id="write-form" on:submit|preventDefault={handleSubmit}>
  <div>
    <label for="">이미지</label>
    <input type="file" bind:files id="image" name="image" />
  </div>
  <div>
    <label for="">제목</label>
    <input type="text" id="title" name="title" bind:value={title} />
  </div>
  <div>
    <label for="">가격</label>
    <input type="number" id="price" name="price" bind:value={price} />
  </div>
  <div>
    <label for="">설명</label>
    <input
      type="text"
      id="description"
      name="description"
      bind:value={description}
    />
  </div>
  <div>
    <label for="">장소</label>
    <input type="text" id="place" name="place" bind:value={place} />
  </div>
  <div>
    <button class="write-button" type="submit">제출</button>
  </div>
  <Footer location="write" />
</form>

<style>
  .write-button {
    padding: 5px 12px 5px 12px;
    background-color: grey;
    border-radius: 10px;
    margin: 10px;
    color: white;
    cursor: pointer;
  }
</style>
