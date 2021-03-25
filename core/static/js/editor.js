document.addEventListener("DOMContentLoaded", function (event) {
  let sc = document.createElement("script");
  sc.setAttribute(
    "src",
    "https://cdn.tiny.cloud/1/4kviqy88krlxrxu48mo5fl42my2dy4pucp6qgkw5yx1nj6gs/tinymce/5/tinymce.min.js"
  );

  document.head.appendChild(sc);

  sc.onload = () => {
    var useDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;

    tinymce.init({
      selector: "#id_content",
      plugins:
        "print preview  importcss  searchreplace autolink autosave save directionality ",
      mobile: {
        plugins:
          "print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker textpattern noneditable help formatpainter pageembed charmap mentions quickbars linkchecker emoticons advtable",
      },
      menu: {
        tc: {
          title: "TinyComments",
          items: "addcomment showcomments deleteallconversations",
        },
      },
      menubar: "file edit view insert format tools table tc help",
      toolbar:
        "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment",
    });
  };
});
