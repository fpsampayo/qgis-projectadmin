--
-- PostgreSQL database dump
--

-- Dumped from database version 9.0.2
-- Dumped by pg_dump version 9.1.3
-- Started on 2012-07-27 13:30:52

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

--
-- TOC entry 447 (class 2612 OID 11574)
-- Name: plpgsql; Type: PROCEDURAL LANGUAGE; Schema: -; Owner: postgres
--

CREATE OR REPLACE PROCEDURAL LANGUAGE plpgsql;


ALTER PROCEDURAL LANGUAGE plpgsql OWNER TO postgres;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 143 (class 1259 OID 57185)
-- Dependencies: 5
-- Name: proyectos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE proyectos (
    id integer NOT NULL,
    proyecto text,
    nombre character varying(100)
);


ALTER TABLE public.proyectos OWNER TO postgres;

--
-- TOC entry 142 (class 1259 OID 57183)
-- Dependencies: 5 143
-- Name: proyectos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE proyectos_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.proyectos_id_seq OWNER TO postgres;

--
-- TOC entry 1790 (class 0 OID 0)
-- Dependencies: 142
-- Name: proyectos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE proyectos_id_seq OWNED BY proyectos.id;


--
-- TOC entry 1781 (class 2604 OID 57188)
-- Dependencies: 142 143 143
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY proyectos ALTER COLUMN id SET DEFAULT nextval('proyectos_id_seq'::regclass);


--
-- TOC entry 1784 (class 2606 OID 57734)
-- Dependencies: 143 143
-- Name: proyectos_pk; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY proyectos
    ADD CONSTRAINT proyectos_pk PRIMARY KEY (id);


--
-- TOC entry 1782 (class 1259 OID 57192)
-- Dependencies: 143
-- Name: proyectos_id_idx; Type: INDEX; Schema: public; Owner: postgres; Tablespace: 
--

CREATE INDEX proyectos_id_idx ON proyectos USING btree (id);


--
-- TOC entry 1789 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2012-07-27 13:30:53

--
-- PostgreSQL database dump complete
--

