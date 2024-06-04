const test = () => {
    try {
        throw new error("This is error");
    } catch (error) {
        return "Inside catch";
    } finally {
        return "Inside Finally";
    }
};

let res = test();
console.log(res);
