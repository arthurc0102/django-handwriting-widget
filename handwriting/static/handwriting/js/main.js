function initSignaturePad(widgetName) {
  console.log('a');
  let canvas = document.getElementById(`id_${widgetName}_canvas`);
  let image_input = document.getElementById(`id_${widgetName}`);
  let signaturePad = new SignaturePad(canvas);

  signaturePad.onEnd = function () {
    image_input.value = signaturePad.toDataURL();
  };

  if (!(image_input.value === '')) {
    signaturePad.fromDataURL(image_input.value, {ratio: 1});
  }
}

function clearSignaturePad(widgetName) {
  let canvas = document.getElementById(`id_${widgetName}_canvas`);
  let image_input = document.getElementById(`id_${widgetName}`);
  let signaturePad = new SignaturePad(canvas);

  signaturePad.clear();
  image_input.setAttribute('value', '');
}
