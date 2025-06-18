const inputNama = document.getElementById("input-nama");
const tombolTambah = document.getElementById("tombol-tambah");
const itemList = document.getElementById("item-list");
let items = []; // Array untuk menyimpan data item (sementara)
let editItemId = null; // Untuk menyimpan ID item yang sedang diedit

// Fungsi untuk menampilkan daftar item
function renderItems() {
  itemList.innerHTML = ""; // Bersihkan daftar sebelum menampilkan ulang
  items.forEach((item, index) => {
    const listItem = document.createElement("li");
    listItem.innerHTML = `
        <span>${item.nama}</span>
        <div class="aksi">
            <button class="edit-button" data-id="${index}">Edit</button>
            <button class="delete-button" data-id="${index}">Hapus</button>
        </div>
    `;
    itemList.appendChild(listItem);
    });

  // Tambahkan event listener untuk tombol edit dan delete setelah item dirender;
  const editButtons = document.querySelectorAll(".edit-button");
  editButtons.forEach((button) => {
    button.addEventListener("click", editItem);
  });

  const deleteButtons = document.querySelectorAll(".delete-button");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", deleteItem);
  });
}

// Fungsi untuk menambahkan item baru
function addItem() {
  const namaItem = inputNama.value.trim();
  if (namaItem) {
    if (editItemId !== null) {

      // Jika sedang dalam mode edit, update item yang ada
      items[editItemId].nama = namaItem;
      editItemId = null; // Reset mode edit
      tombolTambah.textContent = "Tambah";
    } else {

      // Jika tidak dalam mode edit, tambahkan item baru
      items.push({ nama: namaItem });
    }
    inputNama.value = ""; // Bersihkan input
    renderItems(); // Tampilkan daftar item yang sudah diperbarui
  }
}

// Fungsi untuk menghapus item
function deleteItem(event) {
  const itemId = parseInt(event.target.dataset.id);
  items.splice(itemId, 1); // Hapus item dari array berdasarkan index
  renderItems(); // Tampilkan daftar item yang sudah diperbarui

}

// Fungsi untuk menampilkan item yang akan diedit di form
function editItem(event) {
  const itemId = parseInt(event.target.dataset.id);
  const itemToEdit = items[itemId];
  inputNama.value = itemToEdit.nama;
  editItemId = itemId; // Set ID item yang sedang diedit
  tombolTambah.textContent = "Simpan Perubahan";
}

// Event listener untuk tombol tambah

tombolTambah.addEventListener("click", addItem);

// Initial render daftar item (jika ada data awal)
renderItems();
