let graus = 0
basic.forever(function () {
    graus = input.compassHeading()
    if (graus < 45) {
        basic.showString("N ")
    } else if (graus < 135) {
        basic.showString("L ")
    } else if (graus < 225) {
        basic.showString("S ")
    } else if (graus < 315) {
        basic.showString("O ")
    }
})
