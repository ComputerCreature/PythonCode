function read_input_number() {
    var n1 = document.getElementById("input_number").value;
    if (1 <= Number(n1) && Number(n1) <= 10) {
        var countdownSeconds = 3;
        var countdown = function(seconds) {
            if (seconds > 0) {
                document.getElementById("a").innerHTML = `好的，您想要添加${n1}个单词。<br>${seconds}秒后为您跳转……`;
                setTimeout(countdown, 1000, seconds - 1);
            } else {
                    document.getElementById("a").innerHTML = "请在下方的输入框内填写单词相应的信息。";
                    add_code2()
                }
        };
        countdown(countdownSeconds);
    } else {
        document.getElementById("a").innerHTML = "请输入介于 1 和 10 之间的整数。";
    }
}
function add_code1(){
    var code = `
        <p style="text-align: center; color: green; font: 22px '楷体'">好的，请问您要输入几个词语呢？（上限10个）</p>
        <div class="cc">
        <input type="number" name="input_number" id="input_number" min="1" max="10" />
        <input type="button" value="确认" onclick="read_input_number()" />
        </div>
        <p style="text-align: center; color: red; font: 22px '楷体'" id="a"></p>`;
    document.getElementById("b").innerHTML = code;
}
function add_code2(){
    var code = `
        <div class="cc">
            <input type="text" id="word" name="单词" placeholder="请输入单词："></input>
            <input type="button" value="确认"></input>
        </div>
        <div class="cc">
            <input type="text" id="part_of_speech" name="词性" placeholder="请输入词性："></input>
            <input type="button" value="确认"></input>
            <input type="button" value="查看允许词性"></input>
        </div>
        <div class="cc">
            <input type="text" id="pronunciation" name="音标" placeholder="请输入音标："></input>
            <input type="button" value="确认"></input>
        </div>
        <div class="cc">
            <input type="text" id="meaning" name="意思" placeholder="请输入意思："></input>
            <input type="button" value="确认"></input>
        </div>
        `
    document.getElementById("c").innerHTML = code;
}
function input_word()