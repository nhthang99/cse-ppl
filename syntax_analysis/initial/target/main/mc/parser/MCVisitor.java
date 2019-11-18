// Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MCParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MCVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MCParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MCParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#manydcls}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitManydcls(MCParser.ManydclsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#dcls}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDcls(MCParser.DclsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#vardcls}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardcls(MCParser.VardclsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(MCParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#idlist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdlist(MCParser.IdlistContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#funcdcls}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncdcls(MCParser.FuncdclsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#paradcls}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParadcls(MCParser.ParadclsContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#paralist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParalist(MCParser.ParalistContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#paratail}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParatail(MCParser.ParatailContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#para}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPara(MCParser.ParaContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#body}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBody(MCParser.BodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#vardcl_stmt_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardcl_stmt_list(MCParser.Vardcl_stmt_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#vardcl_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardcl_stmt(MCParser.Vardcl_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStmt(MCParser.StmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#assign}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssign(MCParser.AssignContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCall(MCParser.CallContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#explist}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExplist(MCParser.ExplistContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exptail}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExptail(MCParser.ExptailContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#return_t}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturn_t(MCParser.Return_tContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp(MCParser.ExpContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#operand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperand(MCParser.OperandContext ctx);
	/**
	 * Visit a parse tree produced by {@link MCParser#subexp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSubexp(MCParser.SubexpContext ctx);
}