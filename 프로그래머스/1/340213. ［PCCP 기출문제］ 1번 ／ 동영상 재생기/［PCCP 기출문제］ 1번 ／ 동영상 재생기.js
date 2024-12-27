const create_video = () => ({
    video_len: null,
    pos: null,
    op_start: null,
    op_end: null,
})

const parseTime = (str) => {
    const timeRegex = /^(?<mins>[0-5][0-9]):(?<secs>[0-5][0-9])/;
    const { groups: { mins, secs } = {} } = str.match(timeRegex) || {};
    return (+mins) * 60 + (+secs);
}

const stringifyTime = (secs) => {
    const min = Math.floor(secs/60), sec = secs%60
    const [minStr, secStr] = [min, sec].map(v => v < 10 ? `0${v}` : `${v}`)
    return `${minStr}:${secStr}`
}

const movePos = (video, time) => {
    const newPos = video.pos + time;
    video.pos = newPos < 0 ? 0 : newPos > video.video_len ? video.video_len : newPos;
}

const command_skip_openning = (video) => {
    if (video.pos < video.op_start || video.pos >= video.op_end) return;
    video.pos = video.op_end;
}

const commandTable = {
    "prev": (video) => movePos(video, -10),
    "next": (video) => movePos(video, 10),
}
const invokeCommand = (commandString, video) => {
    commandTable[commandString](video);
    command_skip_openning(video);
}

function solution(video_len, pos, op_start, op_end, commands) {
    video = create_video();
    video.video_len = parseTime(video_len);
    video.pos = parseTime(pos);
    video.op_start = parseTime(op_start);
    video.op_end = parseTime(op_end);
    
    command_skip_openning(video)
    commands.forEach(command => invokeCommand(command, video));
    return stringifyTime(video.pos);
}
