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

const move_pos = (video, time) => video.pos += time;
const set_pos = (video, time) => video.pos = time;

const command_skip_openning = (video) => {
    if (video.pos >= video.op_start && video.pos < video.op_end) {
        video.pos = video.op_end;
        command_skip_openning(video);
    }
}

const command_prev = (video) => {
    const amount = -10;
    const thresholdTime = 10;
    if (video.pos < thresholdTime) {
        set_pos(video, 0)
    }
    else {
        move_pos(video, amount);
    }
    command_skip_openning(video);
}

const command_next = (video) => {
    const amount = 10;
    const thresholdTime = video.video_len-10;
    if (video.pos > thresholdTime) {
        set_pos(video, video.video_len) 
    } else {
        move_pos(video, amount);
    }
    command_skip_openning(video);
}


const invokeCommand = (commandString, video) => {
    const table = {
        "prev": command_prev,
        "next": command_next,
    }
    const command =table[commandString];
    command(video);
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
