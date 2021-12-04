const EURviuw = document.querySelector('.eur')
const USDviuw = document.querySelector('.usd')
const eurInRub = document.querySelector('.eur-in-rub')
const eurInput = document.querySelector('.eur-input')
const usdInRub = document.querySelector('.usd-in-rub')
const usdInput = document.querySelector('.usd-input')

const valute = {
    EUR: "",
    USD: ""
}


axios.get("https://v6.exchangerate-api.com/v6/59f1498aca069edffc74243d/latest/BYN")
    .then((res) => {
        valute.EUR = res.data.conversion_rates.EUR
        valute.USD = res.data.conversion_rates.USD
        EURviuw.textContent = valute.EUR
        USDviuw.textContent = valute.USD
    })


eurInput.addEventListener('change', () => {
    if (eurInput.value === '') {
        eurInRub.textContent = 0
    } else {
        eurInRub.textContent = +eurInput.value / valute.EUR + " BYN"
    }
})

usdInput.addEventListener('change', () => {
    if (usdInput.value === '') {
        usdInRub.textContent = 0
    } else {
        usdInRub.textContent = +usdInput.value / valute.USD + " BYN"
    }
})

