fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then(res => {
	  return res.json()
  })
  .then(data => {
	  $('DIV#hello').html(`${data.hello}`)
  })
